# Task 2

# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

# My name is Michele

# Then I would see the string:

#  Michele is name My

# shown back to me.
def reverse_str(string):
    return ' '.join(reversed(string.split()))

if __name__ == "__main__":
    user_string = input('Enter a string of sentence: ')
    print(reverse_str(user_string))