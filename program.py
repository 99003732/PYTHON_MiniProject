import re
class person:
    def __init__(obj,cycle):
        obj.cycle=cycle

    def myfunc(self):
        
        #self.cycle = int(input("Enter the number of words to search :"))
        
        for i in range(0, self.cycle):
            count = 0
            line = 0
            OUTPUT = []

            self.word=str(input("Enter word {} :".format(i+1)))
            pattern = re.compile(self.word, re.I)
            with open('Text.txt', 'rt') as file_info:
                for file_line in file_info:
                    line += 1
                    if pattern.search(file_line) is not None:
                        OUTPUT.append((line, file_line.rstrip('\n')))
                for answer in OUTPUT:
                    count += 1
                    with open("{}.txt".format(self.word), 'a') as file_answer:
                        file_answer.writelines(str(count)+' :')
                        file_answer.writelines(answer[1]+'\n')
            print(count)

p1=person(int(input("Enter the number of words")))
p1.myfunc()
