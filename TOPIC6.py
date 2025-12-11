#TASK1
#def say_hello(name):

#    print(f'Hello, {name}')

#print("You imported hello.py")

#say_hello('user')



#TASK2
# Import the math library for mathematical operations
import math

# This creates a function called "log_info"
# A funciton is a block of reusable code that does a specific task
# "message: str" means this funciton expects a text message as input
# "-> None" means this function doesn't return any value, it just prints smth 
def log_info(message: str) -> None:

 # This line prints (shows on screen) an information message
 # "f" before the string means it is an f-string which lets us insert variables 
 # # {message} will be replaced with the actual message we pass to the function 
 # [INFO] is just a label to show this is an information message 
    print(f"[info] {message}")

# This creates a function called "log_warnign"
# It works the same way as log_info, but for warning messages
def log_warning(message: str) ->None:

    # Prints a warning message with [WARNING] label
    print(f"[WARNING] {message}")

# This creates a function called "log_error"
# It works the same way as the others, but for error messages
def log_error(message: str) -> None:

    # Prints an error message with [ERROR] label 
    print(f"[ERROR] {message}")

# This is our main function that calculates square roots 
# It takes one input called "numbers" which should be a list (collection) of numbers
def calculate_square_root(numbers: list) -> None: