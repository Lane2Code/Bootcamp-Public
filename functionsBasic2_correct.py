#I did some of these on my own & came up with code that gave the correct output. 
#The last 3 i struggled with... A LOT, so I looked up the solution.
# I will do my best to study these & try to learn what works...

# ! Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
print("This is the 'Countdown' activity.")
def countdown(num):
    output = []
    for i in range(num,-1,-1):
        output.append(i)
    return output

print(countdown(5))

# ! Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
print("This is the 'Print & Return' activity.")
def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))


# ! First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
print("This is the 'First Plus Length' activity.")
def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))


# ! Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
#I could not get this on my own. I looked up the solutions and copied it... :(
print("This is the 'Values Greater Than Second' activity.")
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# ! This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
print("This Length, That Value' activity.")
def length_and_value(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))
