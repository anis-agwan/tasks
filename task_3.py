# Task 3

# Take two lists, say for example these two:
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
#
# Extras:
#   1. Randomly generate two lists to test this
#   2. Write this in one line of Python
import random

def common_elements(list_1, list_2):
    return list(set(list_1) & set(list_2))

if __name__ == "__main__":
    list_1 = random.sample(range(1, 50), random.randint(5,10))

    list_2 = random.sample(range(1, 50), random.randint(5,10))

    print(list_1)
    print(list_2)
    print(common_elements(list_1,list_2))