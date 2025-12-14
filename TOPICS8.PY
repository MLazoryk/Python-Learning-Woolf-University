# TASK1
# Import Calable type from typing module
# Callable = smth that can be called like a function
# from typing import Callable

# Define function 'add' that takes two integers and returns integer
# a: int = parameter 'a' must be integer
# b: int = parameter 'b' must be integer
# -> int = function RETURNS an integer
# def add(a: int, b: int) -> int:
#    return a + b # Return sum of a and b

# Define function 'multiply' that takes two integers and retunrs integer
# def multiply(a: int, b: int) -> int:
#    return a * b # Retubr multiplication of a and b

# Callable [[int, int], int] means: 
# [[int, int]] = the function needs 2 integer inputs
# , int] = the function returns 1 integer output
# def apply_operation(a: int, b: int, operation : Callable[[int, int], int]) -> int:
#    return operation(a,b) # Call the operation function with a and b

# Call apply_operations with 'add' function
# operations=add means "use the add funciton"
# result_add = apply_operation(5, 3, add)

# Call apply_operation with 'multiply' function
# result_multiply = apply_operation(5, 3, multiply)

#print(result_add, result_multiply)



# TASK2
# msg = text message to remember
#def outer_fucntion(msg):
    # Save the message in a variable
#    message = msg

#    def inner_function():
#        print(message)
        
        # Give back the inner function (not call it)
#    return inner_function

# my_func = a new function that knows to print "Hello, world!"
#my_func = outer_fucntion("Hello, world!")

# Call the created function
# It print the remembered message
#my_func() # Output: Hello, world!



# TASK3
from typing import Callable

# Function that creates dicount calculators
# discount_percentage = how much % off (like 10 for 10% off)
# Returns: a function that applies that discount to prices
def discount (discount_percentage: int) ->Callable[[float], float]:
