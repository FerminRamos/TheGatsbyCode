# Arrays
rawBookWords = []


def readBook():
    # Defines // Opens a text file
    book = open("Book.txt", "r")

    # Prints Book Title
    print("Reading from book: ", book.name)

    # Grabs all words from a Book, and inserts into many diff. line arrays
    line = book.readlines()
    totalLines = len(line)

    # Makes a single array to hold all words of a book
    currentLine = 0
    currentWord = 0
    # TODO: Clean word before appending to array (No punctuation before or
    #  after), function?
    while currentLine < totalLines:
        '''Splits current line into word arrays'''
        sentence = line[currentLine].split()

        '''Finds Length of Current Sentence (num of words)'''
        totalWords = len(sentence)

        '''Iterates through each word in current sentence'''
        while currentWord < totalWords:
            rawBookWords.append(sentence[currentWord].lower())
            currentWord += 1

        '''Grabs Next Line and Resets Word Count'''
        currentLine += 1
        currentWord = 0

    # Closes Book
    book.close()
