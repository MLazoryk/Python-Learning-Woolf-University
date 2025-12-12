# Requirements:
# Import the math library
# Create three logging functions for info, warnings, and errors
# Make a main function that:
# Takes a list of numbers
# Calculates square roots for non-negative numbers
# Skips negative numbers with a warning
# Handles any errors (like invalid input) with error messages
# Test with a sample list containing different data types
# Run only when the script is executed directly

#import math

# This creates a function called "log_info"
# A function is a block of reusable code that does a specific task
# "message: str" means this function expects a text message as input
# "-> None" means this function doesn't return any value, it just prints something
#def log_info(message: str) -> None:
    # This line prints (shows on screen) an information message
    # "f" before the string means it's an "f-string" which lets us insert variables
    # {message} will be replaced with the actual message we pass to the function
    # [INFO] is just a label to show this is an information message
#    print(f"[INFO] {message}")

# This creates a function called "log_warning"
# It works the same way as log_info, but for warning messages
#def log_warning(message: str) -> None:
    # Prints a warning message with [WARNING] label
#    print(f"[WARNING] {message}")

# This creates a function called "log_error"
# It works the same way as the others, but for error messages
#def log_error(message: str) -> None:
    # Prints an error message with [ERROR] label
#    print(f"[ERROR] {message}")

# This is our main function that calculates square roots
# It takes one input called "numbers" which should be a list (collection) of numbers
#def calculate_square_root(numbers: list) -> None:
    # "for number in numbers:" means "for each item in the numbers list"
    # It goes through the list one item at a time
    # Each time through the loop, the current item is called "number"
#    for number in numbers:
        # "try:" means we're going to try to run some code
        # If something goes wrong (an error), Python will jump to "except"
#        try:
            # "if number < 0:" checks if the current number is less than 0
            # < means "less than", so this checks for negative numbers
            # Square root of negative numbers causes problems in math
#            if number < 0:
                # If the number IS negative, we call our log_warning function
                # We pass it a message that says we found a negative number
#                log_warning(f"Found negative number: {number}. Skipping.")
                # "continue" means "skip the rest of this loop and go to next number"
#                continue

            # If we get here, the number is NOT negative
            # math.sqrt(number) calculates the square root of the number
            # The sqrt() function is inside the math library we imported
#            root = math.sqrt(number)
            # Now we call our log_info function to show the result
            # ":2f" means format the number with 2 decimal places
#            log_info(f"Square root of {number} is {root:.2f}")

        # "except Exception as e:" catches ANY error that happens in the try block
        # "Exception" means any kind of error
        # "as e" means we give the error a name "e" so we can use it
#        except Exception as e:
            # If any error happens, we call our log_error function
            # We pass it a message that says what went wrong
            # {e} will show us the actual error message from Python
#            log_error(f"Error calculating root for {number}: {e}")

# This line checks if this Python file is being run directly
# (not imported by another file)
#if __name__ == "__main__":
    # We create a list of numbers to test our function
    # Lists are created with square brackets []
    # Items in a list are separated by commas
    # This list has: 16, -4, 9, 25, 0, 4, and the text "16" (not a number!)
#    numbers = [16, -4, 9, 25, 0, 4, "16"]
    # This calls our main function and passes it the numbers list
    # The function will process each number in the list
#    calculate_square_root(numbers)


#TASK2
#import math

#def log_info(message: str) -> None: 
#    print(f"[INFO] {message}")

#def log_warning(message: str) -> None: 
#    print(f"[WARNING] {message}")

#def log_error(message: str) -> None:
#    print(f"[ERROR] {message}")

#def calculate_squere_root(numbers: list) -> None: 
#    for number in numbers:
#        try:
#            if number < 0:
#                log_warning(f"Found negative number: {number}. Skipping.")
#                continue
#            root = math.sqrt(number)
#            log_info(f"The square root of {number} is {root:.2f}")
#        except Exception as e: 
#            log_error(f"Error calculating root for {number}: {e}")
#if __name__ == "__main__":
#    numbers = [16, -4, 9, 25, 0, 4, "16"]
#    calculate_squere_root(numbers)



#TASK3
# Requirements: Check if text is same forwards and backwards (ignore spaces/punctuation, ignore uppercase/lowercase)

# s = input text | str text type | bool = returns True/False
def is_palindrome(s: str) -> bool:

    # new_s = empty text container | "" = empty text
    new_s = ""

    # for = loop/cycle | char = each character | in = from inside | input text
    for char in s: 

        # if = check condition | char.isalnum() = "is character letter or number?"
        if char.isalnum():

            # "+=" means add to end | char.lower() = make character lowercase 
            new_s += char.lower()
    
    # s = use cleaned text | = | new_s = our new text (no spaces, lowercase)
    s = new_s

    # return = give answer | s == s[::-1] = "is text equal to reversed text?"
    return s == s[::-1]

# print = show on screen | is_palindrome() = callour funciton | "Козак з казок" = test text
print(is_palindrome("Козак з казок")) # Output: Ture