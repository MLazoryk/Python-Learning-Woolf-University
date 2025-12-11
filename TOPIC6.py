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

    # It goes throgh the list one item at a time
    # Each time through the loop, the current item is called "number"
    for number in numbers: 

        # "try" means we're going to run some code 
        # If something goes wrong (an error), Python will jump to "except"
        try: 

            # < means "less than", so this checks for negative numbers
            # Square root of negative numbers causes problems in math 
            if number < 0: 

                # If the number IS negative, we call out log_warning function
                # WE pass it a message that says we found a negative number
                log_warning(f"Found negative number: {number}. Skipping.")

                # "continue" means skip the rest of this loop and go to next number
                continue

            # If we get here, the number is NOT negative
            # math.sqrt(number) calculates the square root of the number
            # The sqrt() function is inside the math library we imported
            root = math.sqrt(number)

            # Now we call our log_info function to show the result 
            # ":2f" means format the nubmer with 2 decimal places
            log_info(f"Square root of {number} is {root:.2f}")

        # "except Exceptino as e:" catches ANY error that happens in the try block
        # "Exception" means any kind of error
        # "as e" means we give the error a name "e" so we can use it 
        except Exception as e:

            # If any error happens, we call our log_error function
            # We pass it a message that says what went wrong
            # {e} will show us the actual error message from Python
            log_error(f"Error calculating root for {number}: {e}")

    # This line checks if this Python file is being run directly
    # (not imported by another file)
    if __name__ == "__main__":

        # We create a list of numbers to test our function
        # Lists are created with square brackets []
        # Items in a list are separated by commas
        # This list has: 16, -4, 9, 25, 0, 4, and the text "16" (not a number!)
        numbers = [16, -4, 9, 25, 0, 4, "16"]