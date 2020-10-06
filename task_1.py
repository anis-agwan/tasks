# Task 1

# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
def new_list(list):
    first_and_last = [list[0], list[-1]]
    return first_and_last

if __name__ == "__main__":
    user_list = list(map(int, input('Enter space seperated list of numbers: ').split()))
    print(new_list(user_list))