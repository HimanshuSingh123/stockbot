from random import choice, randint
import stocks


def getHello():
    return "wassup"


def stockOptionDescription():
    return "basically gambling but for stocks"


def randomNumber():
    return "you rolled a random number: " + str(randint(1, 10))


def topGainers():
    return stocks.topGainers()


def topLosers():
    return stocks.topLosers()


def relevantStocks():
    return stocks.relevantStocks()


def empty():
    return "You aint send anything"


Responses = {
    "": empty,  # removed parentheses because then it wont call function on dictionary initialization, but rather wait till it gets called by a user via another function
    "hello": getHello,
    "stock options": stockOptionDescription,
    "random number": randomNumber,
    "topgainers": topGainers,
    "toplosers": topLosers,
    "relevantstocks": relevantStocks,
}


def getResponse(input: str):
    lowered: str = input.lower()  # python is case sensitive, makes it easier to process
    print(lowered)
    for key, value in Responses.items():
        if key == lowered:
            return value()
    return choice(["ion understand you", "run that back", "Cant understand you"])


# def getResponse(input: str):
#     lowered: str = input.lower()  # python is case sensitive, makes it easier to process

#     if lowered == "":
#         return "You aint send anything"
#     elif "hello" in lowered:
#         return "wassup"
#     elif "stock options" in lowered:
#         return "basically gambling but for stocks"
#     elif "random number" in lowered:
#         return "you rolled a random number: " + str(randint(1, 10))
#     elif "topGainers" in lowered:
#         return stocks.topGainers()
#     elif "topLosers" in lowered:
#         return stocks.topLosers()
#     elif "relevantStocks" == lowered:
#         return "relevantStocks function is called."
#     else:
#         return choice(["ion understand you", "run that back", "Cant understand you"])
