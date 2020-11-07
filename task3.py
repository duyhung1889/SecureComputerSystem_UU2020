'''
Lab1, Task3: Authentication

Group 6
Student Names: Nike Hiller, Hung Trinh, Bipin Patel, Sanna Regnéll

This file is part of course Secure Computer Systems I at Uppsala University, Sweden.
'''
import random
import math
import string

file = open("words")
content = file.read().splitlines()
nr_words = len(content)
alpha_password = string.ascii_letters + string.digits

def random_password():
    val = int(input("Welcome to the XKCD random password generator, how many words do you want?  "))
    i = 1
    full_psw = ""

    while i <= val: 
        password = random.choice(content)
        full_psw += password + " "
        i += 1
    
    possibilities =nr_words**val
    entropy = math.log(possibilities,2)
    char_set = math.log(62,2)
    random_char = entropy/char_set
    print("\n" + full_psw +"\n" + str(val), "RANDOM words from word list of", nr_words, "words\n" + "Entropy: ", round(entropy,2), "bits\n" + "You need ", round(random_char,2), "RANDOM characters in [a-z A-Z 0-9] to get the same entropy\n")
    

def desired_entropy():
    entropy = float(input("What entropy would you like? "))
    help_math = math.log(nr_words, 2)
    amount_words = math.ceil(entropy / help_math)
    char_set = math.log(62,2)
    nr_char = entropy/char_set

    full_psw = ""
    alpha_full_pws = ""
    i = 0
    
    for password in range(int(amount_words)):
        password = random.choice(content)
        full_psw += password + " "
    
    while i < nr_char:
        char = random.choice(alpha_password)
        alpha_full_pws += char
        i += 1

    print("For the entropy", entropy, "i suggest the password:\n"+"\n"+full_psw+"\nor\n"+alpha_full_pws)

    
random_password()
#desired_entropy()




