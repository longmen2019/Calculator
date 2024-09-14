# """Imports the os and time modules from the Python Standard Library.
# The os module provides a way of using operating system dependent functionality,
# like reading or writing to the file system.
# The time module provides various time-related functions, like getting the current time or pausing
# the execution of the script."""
import os
import time
import statistics
import math

#
# '''Adding a question that ask, what would you like to do, and when the responder said i want to this function or that function it will directily
# take him to the function'''
#
#
def addition(nums):
    """This function asks the user to enter a series of numbers separated by spaces. It then adds all the numbers
    together and returns the result."""
    nums = list(map(float, (input("Enter all numbers separately by space: ").split())))
    return sum(nums)


# # print(addition())
#

def subtraction():
    """This function asks the user to enter a series of number separated by spaces. It then subtracts the second
     number from the first and return the result."""
    # nums_1 = float(input("Enter the first number"))
    # nums_2 = float(input ("Enter the second number"))
    # return nums_1 - nums_2
    nums = list(map(float, input("Enter all numbers separately by space: ").split()))
    result = nums[0]
    for num in nums[1:]:
        result -= num
    return result
#
#
# # print(subtraction())
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


def average():
    """This function takes space space separated number series and then convert it to a list. Then calculates the average
    of that list of numbers."""
    nums = list(map(float, input("Enter all numbers separated by space: ").split()))
    # result = sum(nums)/len(nums)
    # Alternatively, we can use the statistics method, which provides a built-in function for calculating the mean.
    result = statistics.mean(nums)
    return result


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
    try:  # the try block attempts to convert the input to an integer
        nums = int(input("Please enter an integer number: "))
        if nums < 0:
            return "Invalid input: Please enter a non-negative integer."
    except ValueError:
        # if the input is not an integer, a ValueError is raised, and the except block return an "Invalid input" message
        # An additional check ensures the number is non-negative, as functorials are defined for non-negative integers only
        return "Invalid input: Please enter an integer. "

    return math.factorial(nums)

def complex_calculator():
    """
    Function to execute complex arithmetic operations such as addition, subtraction, multiplication, and division.
    Asks the user to choose the operation and input the complex numbers as real and imaginary parts, performs to
    operation, and returns the result.
    """
    print("Enter '1' for complex addition ")
    print("Enter '2' for complex subtraction ")
    print("Enter '3' for complex multiplication")
    print("Enter 4 for complex division")
    choice = input("Enter your choice: ")
    if choice == "1":
        nums = list(map(int, input("Enter all numbers separated by space: ").split()))
        real_sum = sum(nums[0::2])  # Sum of all real parts (even indices)
        imag_sum = sum(nums[1::2])  # Sum of all real parts (odd indices)
        return f"{real_sum} + i{imag_sum}"
    elif choice == "2":
        nums = list(map(int, input("Enter all numbers separated by space: ").split()))
        real_sub = nums[0]
        imag_sub = nums[1]
        for i in range(2, len(nums), 2):
            real_sub -= nums[i]
        for i in range(3, len(nums), 2):
            imag_sub -= nums[i]
        return f"{real_sub} + i{imag_sub}"

    elif choice == "3":
        nums = list(map(int, input("Enter all numbers separated by space: ").split()))
        if len(nums) != 4:
            return "Error: Please enter exactly 4 numbers."
        real = nums[0] * nums[2] - nums[1] * nums[3]
        imag = nums[0] * nums[3] + nums[2] * nums[1]
        return f"{real} + i{imag}"

    elif choice == "4":
        nums = list(map(int, input("Enter all numbers separated by space (exactly 4 elements): ").split()))
        if len(nums) != 4:
            return "Error: Please enter exactly 4 numbers."
        denominator = nums[2] ** 2 + nums[3] ** 2
        if denominator == 0:
            return "Error: Division by zero is not allowed."
        real = (nums[0] * nums[2] + nums[1] * nums[3]) / denominator
        imag = (nums[0] * nums[2] - nums[0] * nums[3]) / denominator
        return f"{real} + i{imag}"


def binomial(nums):
    """
    Function to calculate the binomial coefficient.
    Takes two numbers as arguments, calculates the binomial coefficient using the formula n!/(k!(n-k)!), and returns
    the result.
    """
    result = math.factorial(nums[0]) // (math.factorial(nums[1]) * math.factorial(nums[0] - nums[1]))
    return result

def main():
    while True:
        print(
            "Choose an operation: (addition, subtraction, multiplication, division, average, "
            "factorial, complex_calculator, binomial coefficient, or quit)")
        choice = input().strip().lower()
        if choice == 'addition':
            print(f"Result: {addition()}")
        elif choice == 'subtraction':
            print(f"Result: {subtraction()}")
        elif choice == 'multiplication':
            print(f"Result: {multiplication()}")
        elif choice == 'division':
            print(f"Result: {division()}")
        elif choice == 'average':
            print(f"Result: {average()}")
        elif choice == 'factorial':
            num = int(input("Enter the number: "))
            if num < 0:
                print("Invalid entry")
                continue
            print(f"Result: {factorial(num)}")
        elif choice == 'complex_calculator':
            print(f"Result: {complex_calculator()}")
        elif choice == 'binomial coefficient':
            nums = list(map(int, input("Enter all numbers separated by space (exactly 2 elements): ").split()))
            if len(nums) != 2:
                print("Error: Please enter exactly 2 numbers.")
                continue
            if nums[0] < nums[1]:
                print("Error: The first number must be greater than or equal to the second number.")
                continue
            print(f"Result: {binomial(nums)}")
        elif choice == 'quit':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
