# Task 9

# Please write a binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.

def binary_search(arr, val):
    low = 0
    mid = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < val:
            low = mid + 1
        elif arr[mid] > val:
            high = mid - 1
        else:
            return 'Element is at: ' + str(mid)
        
    return 'Element not in array'

if __name__ == "__main__":
    arr_input = [ 2, 3, 4, 10, 40, 101, 123, 154, 231, 244, 570, 619 ]
    print(arr_input)
    value = int(input('What value do you want to find in the list? '))

    result = binary_search(arr_input, value)
    print(result)