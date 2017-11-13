import json
import os, sys
import time

blue = "\x1b[34m"
red = "\x1b[31m"
green = "\x1b[32m"
white = "\x1b[37m"
yellow = "\x1b[33m"
cyan = "\x1b[36m"
reset = "\x1b[0m"


def load_words():
    try:
        with open("words_dictionary.json", "r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except Exception as e:
        return str(e)


def testHash(hashFn):
    timeStart()
    words = list(load_words().keys())
    timeStop("load words")

    print("You are about to work on ", green, len(words), reset, " words")

    results = {}
    timeStart()
    for word in words:
        hash = hashFn(word)
        if hash in results:
            results[hash].append(word)
        else:
            results[hash] = [word]
    timeStop("iterate over words")

    if len(results) < len(words):
        for hash, innerWords in results.items():
            if len(innerWords) > 1:
                maxFirstTen = innerWords[:10]
                s = ", ".join([str(v) for v in maxFirstTen])
                print(
                    "Found: ", white,
                    s,
                    ", ..." if len(innerWords) > 10 else "",
                    reset,
                    " for ", cyan, hash, reset,
                    " so ", red, len(innerWords), reset, "collisions")
        print("There was a total of ", red, len(words) - len(results), reset, "collisions")
    else:
        print(green, "WOW, no collision", reset)


startTime = 0
endTime = 0

def timeStart():
    global startTime
    startTime = time.time()


def timeStop(key):
    global endTime
    endTime = time.time()

    print(key, "took: ", blue, (endTime - startTime) * 1000, reset)
