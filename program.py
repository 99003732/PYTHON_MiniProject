'''
===========================================================================================================================================
File name        :   Program.py
File Description :   This file contains the logic to find all the
                     occurrances of a given input word in the given text file
File created on  :   25th February, 2021
Time of creation :   21:49:00
Contact info     :   anushka.shivalli@ltts.com
Author           :   Anushka S Shivalli
PS Number        :   99003732
========================================================================================================================================
'''

# Importing the required Modules and packages
import re
import os

# Class to read the number of words


class Word():
    def __init__(self, No_of_words):
        self.No_of_words = No_of_words


# Class Inheritance


class logic(Word):
    # Method to match the given word in the input text file
    def match(self):
        for a in range(0, self.No_of_words):
            self.c = 0
            self.str1 = 0

            # reading the word to search
            word = str(input("Enter word {} :".format(a+1)))
            with open("{}.txt".format(word), 'w') as file_answer:
                with open('Text.txt', 'rt') as file_info:
                    for file_line in file_info:

                        # Use of regular expression to match the word
                        file_line = re.sub(r"\W", " ", file_line)
                        f_l = (file_line).split()
                        for b in range(len(f_l)):

                            # Matching the input_word with all the
                            # possible combinations of letters
                            if word.upper() == f_l[b].upper():
                                if b > 0 and b < (len(f_l)-1):
                                    self.c += 1

                                    # Print word before & after the input_word
                                    x = str(f_l[b - 1] + " " + f_l[b] + " ")
                                    self.str1 = (x + f_l[b + 1] + '\n')
                                    file_answer.writelines(str(self.c)+' :')
                                    file_answer.writelines(self.str1)
                                else:
                                    # Printing the input_word if found at
                                    # the beginning or end of the line
                                    file_answer.writelines(str(self.c+1)+' :')
                                    file_answer.writelines(f_l[b]+'\n')
                                    self.c += 1
            # Checking for the presence of input_word
            if(self.c == 0):
                os.remove("{}.txt".format(word))
                # No creation of __.txt file is word is not found
                print("The word is not found in the given text file")
            else:
                f = open("{}.txt".format(word), 'a')
                f.write("Number of repetition of word is :"+str(self.c))
                f.close()

# Instance creation to the class
p2 = logic(int(input("Enter the number of words to search in file")))

p2.match()   # Method Call
