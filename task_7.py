# Task 7

# Write a password generator in Python. Be creative with how you generate passwords - 
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:
# Ask the user how strong they want their password to be. 
# For weak passwords, pick a word or two from a list.
import string
import random

def pwd_gen(strenth):
    strength = {'weak': 8, 'strong': 12}
    letters = string.ascii_letters
    numbers = string.digits
    puncs = string.punctuation

    if pwd_strength == 'weak':
        chars = letters + numbers
        return ''.join(random.choice(chars) for _ in range(strength[pwd_strength]))
    elif pwd_strength == 'strong':
        chars = letters + numbers + puncs
        return ''.join(random.choice(chars) for _ in range(strength[pwd_strength]))


if __name__ == "__main__":
    while True:
        pwd_strength = str(input('Do you want strong or weak password? ').lower())
        if pwd_strength == 'weak' or pwd_strength == 'strong':
            password = pwd_gen(pwd_strength)
            print('The generated password is: ', password)
            while True:
                new_gen = input('Do you want to generate new one? Yes or No ').lower()
                if new_gen == 'no':
                    print('Selected password: ',password)
                    break
                else:
                    password = pwd_gen(pwd_strength)
                    print('The generated password is: ', password)
            break
        else:
            print('Please choose either weak or strong strength')
            continue


    '''if pwd_strength == 'weak' or pwd_strength == 'strong':
        password = pwd_gen(pwd_strength)
        print('The generated password is: ' + password)
    else:
        print('Please choose either weak or strong strength')'''