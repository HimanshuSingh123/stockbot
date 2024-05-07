from random import choice, randint


def getResponse(input: str):
    lowered: str = input.lower()  # python is case sensitive, makes it easier to process

    if lowered == "":
        return "You aint send anything"
    elif "hello" in lowered:
        return "wassup"
    elif "stock options" in lowered:
        return "basically gambling but for stocks"
    elif "random number" in lowered:
        return "you rolled a random number: " + str(randint(1, 10))
    else:
        return choice(["ion understand you", "run that back", "Cant understand you"])
