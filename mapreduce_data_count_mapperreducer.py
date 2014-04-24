import logging
import sys
import string
import re

# Commented for debugging
#from util import logfile

#logging.basicConfig(filename=logfile, format='%(message)s',
                   #level=logging.INFO, filemode='w')


def word_count():
    # We are going to count the occurences of all the words that appear in the book
    # Alice in Wonderland.
    # 
    # Thus, for this exercise, you need to write a program that will tally
    # the occurences of all the words that appears in Alice in Wonderland serially.
    #
    # The text in Alice in Wonderland will be fed into this program line by line.
    # And you need to write a program that will take each line and do the following:
    # 1) Tokenize a line of text into string tokens, by white space
    #    Example: "Hello, World!" will be converted into "Hello," and "World!"
    #
    # 2) Remove all punctuations
    #    Example: "Hello," and "World!" will be converted to "Hello" and "World"
    #
    # 3) Convert all words into lowercases
    #    Example: "Hello" and "World" will be converted to "hello" and "world"
    #
    # Store the the number of times that a word appears in Alice in Wonderland
    # in the word_counts dictionary
    #
    # Since you are printing the actual output of your program, you
    # can't print a debug statement without breaking the grader.
    # Instead, you should use the logging module which we've configured
    # for you.
    
    # For example:
    # logging.info("My debugging message")
    
    # The logging module can be used to give you more control over your
    # debugging or other messages than you can get by printing them.  In this
    # exercise, print statements will be considered your final output.  By  
    # contrast, messages logged via the logger we configured will be saved to a
    # file.  If you hit "Test Run", then we will show the contents of that file
    # once your program has finished running.  The logging module also has 
    # other capabilities; see https://docs.python.org/2/library/logging.html
    # for more information.


    word_counts = {}

    # debug code: read from file instead of sys.stdin
    f = open('alice/alice.txt', 'r')
    for line in f:

    #for line in sys.stdin:

        #debug print
        print line

        #take the line, split it by spaces
        data = line.strip().split(" ")
        for word in data:
            #remove all non alphanumerics from the word, including spaces, punctuation and then make it lowercase
            word = re.sub(r'[^a-zA-Z0-9]','',word).lower().strip()

            #debug print
            #print word

            #either increment the counter or add it to the dict
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
            
    #debug print            
    print word_counts
    logging.info(word_counts)

if __name__ == "__main__":

    word_count()
