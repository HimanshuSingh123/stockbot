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


def expireyCheck(url: str):
    try:
        r = requests.get(url)
        r.raise_for_status()
        parsedData = r.json()
        # print(parsedData)
        if "Information" in parsedData:
            print(f"Daily API Limit REACHED BRUVVV :{parsedData['Information']}")
            return {
                "error": f"Daily API Limit REACHED BRUVVV :{parsedData['Information']}"
            }
        return parsedData

    except requests.exceptions.HTTPError as e:
        print(e)
        return {"error": f"HTTP ERROR OCCURED BRUV: {e}"}


def relevantStocks():
    # alphavantage stuff - the code below is for news sentiments that talk about what's going on with bigger stocks n stuff
    url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey={getApiKey()}"
    parsedData = expireyCheck(url)
    message = parsedData.get("error", None)
    if message:
        return message
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


# relevantStocks()
# alphavantage stuff - the code below is for news sentiments that talk about what's going on with bigger stocks n stuff


def topGainers():
    url = f"https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={getApiKey()}"
    data = expireyCheck(url)
    message = data.get("error", None)
    if message:
        return message
    i = 0
    # print("last updated:", data["last_updated"])
    print("Top 10 Gainers")
    for item in data["top_gainers"]:
        if i == 10:
            i = 0
            break
        else:
            print(f"Ticker: {item['ticker']}")
            print(f"Price: {item['price']}")
            print(f"Change In Numbers: {item['change_amount']}")
            print(f"Percentage Change: {item['change_percentage']}")
            print(f"Volume: {item['volume']}")
            i += 1


# topGainers()
def topLosers():
    url = f"https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={getApiKey()}"
    data = expireyCheck(url)
    message = data.get("error", None)
    if message:
        return message
    j = 0
    print("Top 10 Losers")
    for item in data["top_losers"]:
        if j == 10:
            j = 0
            break
        else:
            print(f"Ticker: {item['ticker']}")
            print(f"Price: {item['price']}")
            print(f"Change In Numbers: {item['change_amount']}")
            print(f"Percentage Change: {item['change_percentage']}")
            print(f"Volume: {item['volume']}")
            j += 1


# topLosers()


# tker = "AAPL"
# aapl = yf.Ticker(tker)
# # print(aapl.income_stmt)
