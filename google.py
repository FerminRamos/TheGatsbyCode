# Arrays
googleWords = []


def readGoogle():
    # Opens google's dictionary words
    book = open("google-10000-english-no-swears.txt", "r")
    print("Reading from book: ", book.name)

    line = book.read().split("\n")
    totalLines = len(line)

    # Google's 10,000 Words
    currentWord = 0

    # Iteration through google's most used words
    while currentWord < totalLines:
        googleWords.append(line[currentWord])
        currentWord += 1

    # Closes google's dictionary words
    book.close()
