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
#from typing import Callable

# Function that creates dicount calculators
# discount_percentage = how much % off (like 10 for 10% off)
#def discount (discount_percentage: int) ->Callable[[float], float]:
#    def apply_discount(price: float) ->float:
        # Calculate: price - (discount % of price)
        # Example: price = 500, discount = 10%; 500 * (1 - 10/100) = 500 * 0.9 = 450
#        return price * (1 - discount_percentage / 100)
    # Return the discount calculator function
#    return apply_discount

# Create a 10% discount calculator 
# ten_percent_discount = function that gives 10% off any price 
#ten_percent_discount = discount(10)

# Create a 20% discount calculator
# twenty_percent_discount = function that gives 20% any price
#twenty_percent_discount = discount(20)

# Use 10% discount on 500$
# 500 - 10% = 500 * 0.9 = 450
#discounted_price = ten_percent_discount(500) # Result: 450.0
#print(discounted_price)

# Use the 20% discount on 500$
# 500 - 20% = 500 * 0.8 = 400
#discounted_price = twenty_percent_discount(500) # 400.0
#print(discounted_price)



# TASKS4
class Solution (object):
    def twoSum (self, nums, target): 
        # self = is required
        # nums = is our list of numberts (like[1,2,3,4])
        # target = is the number we wanna to reach (like 9)

        seen = {}
        # an enpty dictionary 

        for i, num in enumerate(nums):
            # "enumerate(nums)"" gives us both, the POSITION = "i", and the VALUE = "num".
            # E.g. [55, 0, 607....] 
            # the firsy loop gives us the [0, 55]

            needed = target - num 
            # Calculate what nubmer we need to complete the pair  
            # E.g. if current nnumber is 2, and the target is 9 
            # We need 9 - 2 = 7


            if needed in seen: 
                # check of this needed number exists in our dictionary

                return[seen[needed], i]
                # Return the positions of numbers 
                # "[seen[needed]]" gives the positon where we saw the "needednumber"
                # "i" is the current Position 
                # So we return [position_of_needed, current_position]

            seen[num] = i
            # if we didn't find the pair yer, store current number
            # add this nubmer to our dictionary so we remeber we so it

        return []
    # This line runs only we NO solution is found 
    # But the problam says there is always the solution, so we don't reach here


# Test your function
# Create an instance of the Solution class called 'sol'
# This lets us use the twoSum method inside it
sol = Solution()

# Call the twoSum method with list [2,7,11,15] and target 9
# Should return [0,1] because 2 (index 0) + 7 (index 1) = 9
print(sol.twoSum([2,7,11,15], 9))  # Expected: [0,1]

# Call twoSum again with different input: [3,2,4] and target 6
# Should return [1,2] because 2 (index 1) + 4 (index 2) = 6
print(sol.twoSum([3,2,4], 6))      # Expected: [1,2]
