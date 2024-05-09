import yfinance as yf
import pandas as pd
import alpha_vantage as av
from dotenv import load_dotenv
import os
import requests
from datetime import datetime


load_dotenv()


def getApiKey():
    return os.getenv("alphaVanKey")


def timeConvert(time: str) -> str:
    parsedTime = datetime.strptime(time, "%Y%m%dT%H%M%S")
    return parsedTime


def relevantStocks():
    # alphavantage stuff - the code below is for news sentiments that talk about what's going on with bigger stocks n stuff
    url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey={getApiKey()}"
    r = requests.get(url)
    parsedData = r.json()
    for item in parsedData["feed"]:
        for topic in item["topics"]:
            relevance = float(topic["relevance_score"])  # conv to float
            if relevance > 0.9:
                print("Topics: ")
                print("- Topic:", topic["topic"])
                print("  Relevance Score:", topic["relevance_score"])

        # print data if relevance is high
        if relevance > 0.9:
            print("\nTitle:", item["title"])
            print("URL:", item["url"])
            print("Time Published:", timeConvert(item["time_published"]))
            print("Authors:", ", ".join(item["authors"]))
            print("Summary:", item["summary"])
            print("Source:", item["source"])
            print("Ticker Sentiments:")
            for ticker_sentiment in item["ticker_sentiment"]:
                print("- Ticker:", ticker_sentiment["ticker"])
                print("  Relevance Score:", ticker_sentiment["relevance_score"])
                print("  Sentiment Score:", ticker_sentiment["ticker_sentiment_score"])
                print("  Sentiment Label:", ticker_sentiment["ticker_sentiment_label"])
    # alphavantage stuff - the code below is for news sentiments that talk about what's going on with bigger stocks n stuff


def topGainers():
    url = f"https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={getApiKey()}"
    r = requests.get(url)
    data = r.json()
    print(data)


# relevantStocks()
topGainers()

tker = "AAPL"
aapl = yf.Ticker(tker)
# print(aapl.income_stmt)
