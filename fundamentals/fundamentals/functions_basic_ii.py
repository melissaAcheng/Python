# 1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

list = [];
def countdown(num):
    for x in range(num, -1, -1):
        list.append(x)

countdown(5)
print(list)

# 2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def print_return(num_list):
    print(num_list[0])
    return num_list[1]

y = print_return([1,2])
print(y)

# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def first_plus_length(list_2):
    return list_2[0] + len(list_2)

print(first_plus_length([1,2,3,4,5]))

# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False


def create_list(og_list):
    if len(og_list) < 2:
        return False
    new_list = []
    count = 0
    for i in range(0, len(og_list)):
        if og_list[i] > og_list[1]:
            new_list.append(og_list[i])
            count += 1
    print(count)
    return(new_list)

print(create_list([5,2,3,2,1,4]))

# 5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

list_3 = []

def size_value(size, value):
    for x in range(0, size):
        list_3.append(value)
    return list_3

print(size_value(6,2))