# This program will ONLY make prophecies from entire words of a textbook.
#  It will not try to pull individual letters and make words out of it.

# imports
# import dictionary.py later, when everything is written in...
import google
import book


# TODO: THIS IS Gatsby BOOK'S SPOT!!!!
book.readBook()
# TODO: THIS IS Gatsby BOOK'S SPOT!!!!


# TODO: THIS IS GOOGLE'S SPOT!!!!
google.readGoogle()
# TODO: THIS IS GOOGLE'S SPOT!!!!


# WordBank, stores list of all usable words from book.
wordBank = []


# Cleans up a word so it doesn't have any punctuation attached & appends
#  to word bank.
def addWord(word):
    # List of Special Characters
    regularChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z', "'"]

    # Array that holds a word without special chars
    cleanWord = ""
    word.split()
    wordSize = len(word)
    i = 0

    # Iterates through our inputted word
    while i < wordSize:
        # Iterates through our regular chars
        c = 0
        while c < 27:
            if word[i] == regularChars[c]:
                # Add letter to cleanWord array
                cleanWord += word[i]
                break
            # Next Char in Alphabet
            c += 1
        # Next Char in Word
        i += 1

    # Adds word to word bank
    wordBank.append(cleanWord)


# Grabs chars in line based on skipCode.
skipCode = 2
totalWords = len(book.rawBookWords)
currentWord = 0
while currentWord < totalWords:
    if currentWord % skipCode == 0:
        addWord(book.rawBookWords[currentWord])
        '''wordBank.append(wordArray[currentWord])'''
    currentWord += 1


# REFORMAT Dictionary.py to be used as code....save as a separate file, as
# archive!
book = open("dictionary.py", "w")
currentWord = 0
book.write("dictionary = {")
while currentWord < len(google.googleWords):
    book.write('"')
    book.write(google.googleWords[currentWord])
    book.write('": "')
    book.write("0")
    book.write('"')
    if currentWord != len(google.googleWords) - 1:
        book.write(", ")
    book.write("\n")
    currentWord = currentWord + 1
book.write("}\n")
book.close()
# Test Dictionary


# TODO: This is for the main part of your code that makes
#  sentences. You'll have an array of different word types
#  (nounArray, verArray, etc.). You need to match words from
#  your word bank with a hashmap of all the different words
#  from the dictionary. If wordBank word matches key, then
#  check that key's value to see what word type it is (verb,
#  noun, etc.). If noun, then move word from wordBank array
#  to nounArray.
#  Moving On, you're going to make a while loop ( i < 3) to
#  make 3 sentences. Inside of that, you're going to have a
#  random number generator that tells you what type of
#  sentence to make (verb first, then noun, etc. OR
#  noun first, then verb, etc.). The random number generator
#  will give you an option of 1-3 (or more if you choose to
#  expand). This corresponds to a branch of a switch statement
#  (Ex, branch 1 = #1). Inside each branch, you're going to
#  switch (hahaha, get it?) the order in which you're going to
#  pick // print the words from the nouns//verbs arrays. To
#  avoid repeating code, just make a function that receives
#  an array -> calls the random num generator -> and outputs
#  a word from the array. Which array is passed is up to the
#  switch branches.

# TODO: Tense is important! Figure out how how read past, present,
#  and future tense for sentences. ***PROGRAM IS ABOUT PROPHECY!!!!***
#  So only future // past tense words shall be used!!!!! (Bc future-only
#  tense doesn't have a lot of combinations for word structures)
