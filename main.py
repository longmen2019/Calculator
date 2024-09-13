"""Imports the os and time modules from the Python Standard Library.
The os module provides a way of using operating system dependent functionality,
like reading or writing to the file system.
The time module provides various time-related functions, like getting the current time or pausing
the execution of the script."""
import os
import time
import statistics
import math


def addition():
    """This function asks the user to enter a series of numbers separated by spaces. It then adds all the numbers
    together and returns the result."""
    nums = list(map(float,(input("Enter all numbers separately by space: ").split())))
    return sum(nums)
# print(addition())

def subtraction():
    """This function asks the user to enter a series of number separated by spaces. It then subtracts the second
     number from the first and return the result."""
    # nums_1 = float(input("Enter the first number"))
    # nums_2 = float(input ("Enter the second number"))
    # return nums_1 - nums_2
    nums = list(map(float, input("Enter all numbers separately by space: ").split()))
    result = nums[0]
    for num in nums[1:]:
        result -=num
    return result
# print(subtraction())
def multiplication():
    """This function asks the user to enter a series of number separated by spaces. It then multiply all the numbers
    together and return the result."""
    nums = list(map(float, (input("Enter all numbers separately by space: ").split())))
    result = nums[0]
    for num in nums[1:]:
        result *= num
    # # Alternative method
    # result = 1
    # for num in nums:
    #     result *= num
    return result
# print(multiplication())

def division():
    """This function asks the user to enter a series of numbers separated by spaces. It then divides the first number
    by each of the subsequent numbers and return the result."""
    nums = list(map(float, input("Enter all numbers separately by space: ").split()))
    result = nums[0]
    for num in nums[1:]:
        if num == 0:
            return "Invalid Entry"
        else:
            result /= num
    return result

    # # Alternative method
    # """Function divide two numbers"""
    # n1 = float(input("Enter first number: "))
    # n2 = float(input("Enter second number: "))
    # if n2 == 0:
    #     # print("Invalid entry")
    #     return "Invalid entry"
    # # print( n1/n2)
    # return n1/n2

# # Example usage
# print(division())

def average():
    """This function takes space space separated number series and then convert it to a list. Then calculates the average
    of that list of numbers."""
    nums = list(map(float,input("Enter all numbers separated by space: ").split()))
    # result = sum(nums)/len(nums)
    # Alternatively, we can use the statistics method, which provides a built-in function for calculating the mean.
    result = statistics.mean(nums)
    return result
# # Example usage
# print(average())

def factorial():
    """ Function to calculate the factorial of a number. Takes a number as an argument,
    calculates the factorial of the number, and returns the result"""
    # nums = int(input("Please enter an integer number: "))
    # result = 1
    # for num in range(nums):
    #     result *= num + 1
    # return result
    """Another approach is to use math module, which provides a built-in factorial function"""
    """Add an if statement to check if the input is an integer and return an "Invalid input" message if it's not."""
    try: # the try block attempts to convert the input to an integer
        nums = int(input("Please enter an integer number: "))
        if nums < 0:
            return "Invalid input: Please enter a non-negative integer."
    except ValueError:
        # if the input is not an integer, a ValueError is raised, and the except block return an "Invalid input" message
        # An additional check ensures the number is non-negative, as functorials are defined for non-negative integers only
        return "Invalid input: Please enter an integer. "

    return math.factorial(nums)
# Example usage
print(factorial())

