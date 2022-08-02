#############################################################################################################
# Assignment:
# Author:              Peter Pham (pxp180041)
# Course:              CS 4348.002
# Date Started:        02/08/2022
# IDE:                 pycharm
#
# Description:
#
#############################################################################################################

################# I M P O R T S #################
import re
import nltk
import random
import enchant
import contractions
import pyperclip3 as pc
from random import sample
from urllib import request
from bs4 import BeautifulSoup
from nltk.corpus import words


#############################################################################################################
#  * Function:            main
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        02/08/2022
#  *
#  * Description:
#  * Main driver of the program. Calls all the other functions to accomplish the task assigned.
#############################################################################################################
def main():

    
    length, punctuation = menu()

    text = generate_sentence(length)

    print(text)
    
    if not punctuation:
        text = remove_punc(text)
    
    output(text)

    print("done")


#############################################################################################################
#  * Function:            main
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        02/08/2022
#  *
#  * Description:
#  * Main driver of the program. Calls all the other functions to accomplish the task assigned.
#############################################################################################################
def menu():

    length = int()
    valid_input = False

    # Short or long sentences
    while not valid_input:
        try:
            print("1. Short")
            print("2. Medium")
            print("3. Long")
            length = int(input("Select an option: "))

            if length < 1 or length > 3:
                raise TypeError

            valid_input = True

        except:
            print("Invalid input try again!\n\n")

    valid_input = False

    # include punctuation or no
    while not valid_input:
        punctuation = input("Include punctuation? (Y/N): ")
        if punctuation.lower() == "y" or punctuation.lower() == "yes":
            punctuation = True
            valid_input = True

        elif punctuation.lower() == "n" or punctuation.lower() == "no":
            punctuation = False
            valid_input = True

        else:
            print("Invalid input try again!\n\n")

    return length, punctuation

#############################################################################################################
#  * Function:            main
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        02/08/2022
#  *
#  * Description:
#  * Main driver of the program. Calls all the other functions to accomplish the task assigned.
#############################################################################################################
def generate_sentence(length):

    corpus = nltk.corpus.brown.sents(categories=['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies',
                                               'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance',
                                               'science_fiction'])

    text = random.choice(corpus)

    if length == 1:
        while True:
            if len(text) < 15:
                return text
            else:
                text = random.choice(corpus)

    elif length == 2:
        while True:
            if len(text) > 16 and len(text) < 20:
                return text
            else:
                text = random.choice(corpus)

    elif length == 3:
        while True:
            if len(text) > 21:
                return text
            else:
                text = random.choice(corpus)

#############################################################################################################
#  * Function:            main
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        02/08/2022
#  *
#  * Description:
#  * Main driver of the program. Calls all the other functions to accomplish the task assigned.
#############################################################################################################
def remove_punc(text):

    fixed = []

    for word in text:
        fixed_word = contractions.fix(word)
        fixed_word = re.sub(r'[^\w\s]', '', word)

        if fixed_word != "":
            fixed.append(fixed_word)

    return fixed

#############################################################################################################
#  * Function:            main
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        02/08/2022
#  *
#  * Description:
#  * Main driver of the program. Calls all the other functions to accomplish the task assigned.
#############################################################################################################
def output(text):
    text = ' '.join(text)
    print(text)
    print("Copied to clipboard")
    pc.copy(text)


#############################################################################################################
#  * Function:            main
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        02/08/2022
#  *
#  * Description:
#  * Main driver of the program. Calls all the other functions to accomplish the task assigned.
#############################################################################################################
def word_list_generator():
    url = "https://www.mit.edu/~ecprice/wordlist.10000"

    d = enchant.Dict("en_US")

    html = request.urlopen(url)

    list_words = list()

    soup = BeautifulSoup(html, "lxml")
    raw = soup.get_text()

    with open("a.txt", "w") as file:
        for line in raw.splitlines():
            if (d.check(line)) and (len(line) > 2):
                file.write(line + " ")


#############################################################################################################
#  * Function:            main
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        02/08/2022
#  *
#  * Description:
#  * Main driver of the program. Calls all the other functions to accomplish the task assigned.
#############################################################################################################
def generate_word():
    word_count = 10

    key_set = get_keys(set([1, 2, 3]))

    result = set()

    while len(result) < word_count - 1:
        valid_word = False
        
        while not valid_word:
            # generate a word
            random_word = ' '.join(sample(words.words(), 1))

            # see if the word is in the specified list
            for word in random_word:
                if word not in key_set:
                    valid_word = False
                    break
                else:
                    valid_word = True

            if valid_word:
                result.add(random_word)
                print("added a word: " + random_word)


    print("done")


#############################################################################################################
#  * Function:            main
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        02/08/2022
#  *
#  * Description:
#  * Main purpose is to check for arguments and start main function
#  *
#  * Parameters:
#############################################################################################################
def get_keys(key_list):

    top_row = set([char for char in "qwertyuiop"])
    home_keys = set([char for char in "asdfghjkl;"])
    bottom_row = set([char for char in "zxcvbnm"])

    key_set = set()

    if 1 in key_list:
        key_set.update(top_row)
    if 2 in key_list:
        key_set.update(home_keys)
    if 3 in key_list:
        key_set.update(bottom_row)

    return key_set

    
#############################################################################################################
#  * Function:            main
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        02/08/2022
#  *
#  * Description:
#  * Main purpose is to check for arguments and start main function
#  *
#  * Parameters:
#############################################################################################################
if __name__ == '__main__':
    main()
