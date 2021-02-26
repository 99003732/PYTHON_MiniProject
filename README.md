# PYTHON_MiniProject
Python_Mini_Project

The code contains 2 classes:
1. Class name  :  Word
   description : This class contains the code to read the number of input words to be searched

2. Class name  :  logic 
                  The Word class has been inherited in logic class which matches the given input word with the input text file
       
Logic to find the input word:

1. From the input file, each line is extracted and is put in a list
2. The input word and its index is searched in the list
3. If the word is found in the indices other than 0 and end-1, then the input word along with its previous and 
   next words are printed in the new text file with the name as the input word
4. Else, only the input word is printed.
5. If the given input word is not found in the input text file, the text file is not created for it to save the memory. 
6. Instead, the message is popped up to the user as : The word is not found in the file. 

Total no. of classes : "2" |-------
Total no. of methods : "2" |-------
Total objects        : "1" |

sample inputs    |     sample outputs|-----

software         |    **"software.txt"**|-----
                      ..... software .....  (word not found at index 0 and end-1)|-----
                      software              (word found at index 0 or end-1)|-----
                      Total number of repitition of word is ....|
                      
soft             |     The word is not found in the given input file|
                      
                      
