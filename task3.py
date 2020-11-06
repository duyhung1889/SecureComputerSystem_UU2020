import random
import math 

file = open("words")
content = file.read().splitlines()


def random_password():
    val = int(input("Welcome to the XKCD random password generator, how many words do you want?  "))
    nr_words = len(content)
    i = 1
    full_psw = ""
    total_len = 0

    while i <= val: 
        password = random.choice(content)
        full_psw += password + " "
        word_len = len(password)
        total_len += word_len
        i += 1
    
    possibilities = nr_words**val
    entropy = math.log(possibilities,2)
    print('\n' + full_psw )
    print(val, 'RANDOM words from word list of', nr_words, 'words')
    print("Entropy: ", entropy, "bits")
    
        
 



random_password()