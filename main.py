import random


def create_random_list(count, range_from, range_to):
    random_list = []
    while len(random_list) < count:
        random_list.append(random.randint(range_from, range_to))
    return random_list


def check_list_contains_item(number_of_item, li):
    i = 0
    while i < len(li):
        if i == number_of_item:
            i += 1
            continue
        elif li[i] == li[number_of_item]:
            return True
        i += 1
    return False


if __name__ == '__main__':

    # Task 1
    """
    # The greatest number
    #
    # Write a Python program to get the largest number from a list of random numbers with the length of 10
    #
    # Constraints: use only while loop and random module to generate numbers
    """
    arr = create_random_list(10, 1, 100)
    i = 0
    temp = 0
    print(f"We have this list: {arr}")
    while i < len(arr):
        if arr[i] > temp:
            temp = arr[i]
        i += 1
    print(f"\033[33mThe greatest number of list -> {temp} \033[0m")

    # Task 2
    """
    Exclusive common numbers.

    Generate 2 lists with the length of 10 with random integers from 1 to 10,
    and make a third list containing the common integers between the 2 initial lists without any duplicates.

    Constraints: use only while loop and random module to generate numbers
    """
    arr = create_random_list(10, 1, 10)
    brr = create_random_list(10, 1, 10)
    crr = arr + brr
    print(f"List before -> \033[31m{crr}\033[0m")
    i = 0
    while i < len(crr):
        if check_list_contains_item(i, crr):
            crr = crr[:i] + crr[i + 1:]
            continue
        i += 1
    print(f"List after  -> \033[32m{crr}\033[0m")

    # Task 3
    """
    Extracting numbers.
    
    Make a list that contains all integers from 1 to 100, 
    then find all integers from the list that are divisible by 7 but not a multiple of 5, 
    and store them in a separate list. Finally, print the list.
    
    Constraint: use only while loop for iteration
    """

    i = 0
    n = 100
    arr = []
    brr = []
    while i < n:
        arr = arr + [i + 1]
        if arr[i] % 7 == 0 and not arr[i] % 5 == 0:
            brr = brr + [arr[i]]
        i += 1
    print(f"List of number divisible by 7 and not multiple of 5: \n{brr}")