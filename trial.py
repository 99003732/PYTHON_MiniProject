import re
import os


class Word():
    def __init__(self, No_of_words):
        self.No_of_words = No_of_words
        self.c = 0
        self.str1 = 0


class logic(Word):
    def match(self):
        for a in range(0, self.No_of_words):
            word = str(input("Enter word {} :".format(a+1)))
            with open("{}.txt".format(word), 'w') as file_answer:
                with open('Text.txt', 'rt') as file_info:
                    for file_line in file_info:
                        file_line = re.sub(r"\W", " ", file_line)
                        f_l = (file_line).split()
                        for b in range(len(f_l)):
                            if word.lower() == f_l[b].lower():
                                if b > 0 and b < (len(f_l)-1):
                                    self.c += 1
                                    self.str1 = (f_l[b-1]+" "+f_l[b]+" "+f_l[b+1]+'\n')
                                    file_answer.writelines(str(self.c)+' :')
                                    file_answer.writelines(self.str1)
                                else:
                                    file_answer.writelines(str(self.c+1)+':')
                                    file_answer.writelines(f_l[b]+'\n')
                                    self.c += 1
            if(self.c == 0):
                os.remove("{}.txt".format(word))
                print("The word is not found in the given text file")
            else:
                f = open("{}.txt".format(word), 'a')
                f.write("Total number of occurence:"+str(self.c))
                f.close()

p2 = logic(int(input("Enter the number of words")))
p2.match()
