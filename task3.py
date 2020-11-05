import random

file = open("words")
content = file.read().splitlines()

def random_password():
    val = int(input("Welcome to the XKCD random password generator, how many words do you want?  "))
    i = 1
    full_psw = ""
    nr_words = len(content)
    while i <= val: 
        password = random.choice(content)
        full_psw += password + " "
        i += 1
    
    print('\n' + full_psw )
    print(val, 'RANDOM words from word list of', nr_words, 'words')
        
 



random_password()