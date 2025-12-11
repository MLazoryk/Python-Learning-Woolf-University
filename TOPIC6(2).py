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


import math

def log_info(message: str) -> None: 
    print(f"[INFO] {message}")

def log_warning(message: str) -> None: 
    print(f"[WARNING] {message}")

def log_error(message: str) -> None:
    print(f"[ERROR] {message}")

def calculate_squere_root(numbers: list) -> None: 
    for number in numbers:
        try:
            if number < 0:
                log_warning(f"Found negative number: {number}. Skipping.")
                continue
            root = math.sqrt(number)
            log_info(f"The square root of {number} is {root:.2f}")
        except Exception as e: 
            log_error(f"Error calculating root for {number}: {e}")
if __name__ == "__main__":
    numbers = [16, -4, 9, 25, 0, 4, "16"]
    calculate_squere_root(numbers)
