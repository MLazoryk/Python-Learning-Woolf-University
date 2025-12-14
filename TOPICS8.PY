# Import Calable type from typing module
# Callable = smth that can be called like a function
from typing import Callable

# Define function 'add' that takes two integers and returns integer
# a: int = parameter 'a' must be integer
# b: int = parameter 'b' must be integer
# -> int = function RETURNS an integer
def add(a: int, b: int) -> int:
    return a + b # Return sum of a and b

# Define function 'multiply' that takes two integers and retunrs integer
def multiply(a: int, b: int) -> int:
    return a * b # Retubr multiplication of a and b

# Callable [[int, int], int] means: 
# [[int, int]] = the function needs 2 integer inputs
# , int] = the function returns 1 integer output
def apply_operation(a: int, b: int, operation : Callable[[int, int], int]) -> int:
    return operation(a,b) # Call the operation function with a and b

# Call apply_operations with 'add' function
# operations=add means "use the add funciton"
result_add = apply_operation(5, 3, add)

