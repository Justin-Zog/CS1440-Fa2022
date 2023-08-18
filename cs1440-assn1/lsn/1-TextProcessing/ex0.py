# Justin Herzog A02306067
def findWords(sentence):
    # wordsToReturn = []
    wordsToReturn = sentence.split()
    wordsToRemove = []
    # Make a list of illegal words
    for i in wordsToReturn:
        if len(i) > 5:
            wordsToRemove.append(i)
    # Remove those words
    for i in wordsToRemove:
        wordsToReturn.remove(i)

    return wordsToReturn


if __name__ == '__main__':
    provided = [
        "Craftsman Keep Reveal personal it harmful engine short friendly killer honest season and camera strange hiccup horseshoe sphere charismatic ceiling sweet formation substitute daughter perfect",
        "Keep reject",
        "Do or do not, there is no try.",
        "TechnicallyI'mOneWordOnly",
        "One two skip a few, 99 100!"
    ]

    resultList = []
    for string in provided:
        resultList.append(findWords(string))

    for result in resultList:
        print(result)

    # Should Output:
        # ['Keep', 'it', 'short', 'and', 'sweet']
        # ['Keep']
        # ['Do', 'or', 'do', 'not,', 'there', 'is', 'no', 'try.']
        # []
        # ['One', 'two', 'skip', 'a', 'few,', '99', '100!']
