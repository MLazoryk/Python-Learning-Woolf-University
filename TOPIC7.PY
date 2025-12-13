# TASK 1
# Function to create an empty stack
# Stack = data structure like a pile of plates - last in, first out (LIFO)
#def create_stack():
#    return []  # Return an empty list (list will act as our stack)

# Function to check if stack is empty
#def is_empty(stack):
#    return len(stack) == 0  # True if stack has no elements (0 items)

# Function to add element to top of stack
# Append = add to the end
#def push(stack, item):
#    stack.append(item)  # Add item to end of list (top of stack)

# Function to remove element from top of stack
# Pop = remove the last/top element
#def pop(stack):
#    if not is_empty(stack):  # Check if stack is not empty
#        return stack.pop()  # Remove and return last element (from top)
#    else:
#        print("Стек порожній")  # Print error message (Stack is empty)

# Function to view top element without removing it
# Peek = look at the top element without removing it
#def peek(stack):
#    if not is_empty(stack):  # Check if stack is not empty
#        return stack[-1]  # Return last element (top of stack)
#    else:
#        print("Стек порожній")  # Print error message (Stack is empty)


# Create a new stack (initialize an empty stack)
#stack = create_stack()

# Add three elements to stack (push them onto stack)
#push(stack, 'a')  # Stack: ['a'] - add 'a' to stack
#push(stack, 'b')  # Stack: ['a', 'b'] - add 'b' to top
#push(stack, 'c')  # Stack: ['a', 'b', 'c'] - add 'c' to top

# Show current stack (display all elements)
#print("Поточний стек:", stack)  # Output: ['a', 'b', 'c']

# Show top element (look at what's on top without removing)
#print("Верхній елемент:", peek(stack))  # Output: 'c' (last element added)

# Remove top element (take 'c' off the stack)
#print("Видалений елемент:", pop(stack))  # Output: 'c' (removed element)

# Show stack after removing top (what's left in stack)
#print("Стек після pop:", stack)  # Output: ['a', 'b'] (now 'b' is on top)

# Check if stack is empty (is there anything left?)
#print("Стек порожній?", is_empty(stack))  # Output: False (not empty, has 2 items)

# Remove remaining elements (take elements off one by one)
#pop(stack)  # Removes 'b' -> Stack: ['a'] (top element 'b' removed)
#pop(stack)  # Removes 'a' -> Stack: [] (last element 'a' removed)

# Check if stack is empty now (all elements removed)
#print("Стек порожній?", is_empty(stack))  # Output: True (stack is now empty)

# Вихід програми буде виглядати так:
# Поточний стек: ['a', 'b', 'c']
# Верхній елемент: c
# Видалений елемент: c
# Стек після pop: ['a', 'b']
# Стек порожній? False
# Стек порожній? True



#TASK2
#import collections

#Cat = collections.namedtuple('Cat',['nickname','age','owner'])
#cat = Cat('Mafia', 4, 'Robert')

#print(f"This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}")



#TASK3
#student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]

# Empty dictionary to store mark counts
#mark_counts = {}

# Loop through each mark in the list
#for mark in student_marks:

    # Check if mark already exists in dictionary
#    if mark in mark_counts:

        # Increment count if mark exists
#        mark_counts[mark] += 1

#    else:

        # Imitialize count to 1 if mark doesn't exist
#        mark_counts[mark] = 1

# Print the final dictionary with mark frequencies        
#print(mark_counts)



# TASK4 (same task as previous)
#import collections

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]

# mark_counts = collections.Counter(student_marks)



# TASK5
#import collections
#student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]

#mark_counts = collections.Counter(student_marks)

#print (mark_counts.most_common())
#print (mark_counts.most_common(1))
#print (mark_counts.most_common(2))




# TASK6
#from collections import Counter

#letter_count = Counter("banana")
#print(letter_count)



# TASK7
#from collections import Counter

#sentence = "the quick brown for jumps over the lazy dog"

#Split the sentence onto individual words 
#words = sentence.split()

#word_count = Counter(words)

#for word, count in word_count.items():
#    print(f"{word}: {count}")



#TASK8 
#import collections 

#Person = collections.namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

#person = Person('Maks', 'Lazoryk', 18, 'Lviv', '01146')

#print(person.first_name)
#print(person.last_name)
#print(person.age)
#print(person.birth_place)
#print(person.post_index)



# TASK9
# Import deque from collections module
# from collections import deque

# Create an empty queue
# queue = deque()

# Add 'a' to the end of queue (enqueue operation)
# queue.append('a')

# Add 'b' to the end of queue (enqueue operation)
# queue.append('b')

# Add 'c' to the end of queue (enqueue operation)
# queue.append('c')

# Print queue after adding elements
# list(queue) converts deque to list for display
# print("Черга після додавання елементів:", list(queue))

# Remove and return first element (dequeue operation)
# popleft() removes from left/front of queue
# print("Видалений елемент:", queue.popleft())

# Print queue after removing first element
# print("Черга після видалення елемента:", list(queue))

# Peek at first element without removing
# queue[0] accesses first element
# print("Перший елемент у черзі:", queue[0])

# Check if queue is empty
# len(queue) == 0 checks if length is zero
# print("Чи черга порожня:", len(queue) == 0)

# Get size of queue
# len(queue) returns number of elements
# print("Розмір черги:", len(queue))

# Expected output:
# Черга після додавання елементів: ['a', 'b', 'c']
# Видалений елемент: a
# Черга після видалення елемента: ['b', 'c']
# Перший елемент у черзі: b
# Чи черга порожня: False
# Розмір черги: 2



# TASK10
from collections import deque 

# Create an empty deque
d = deque()

# Add 'middle' to the right end of deque
d.append('middle')

# Add 'Last' to the right end of deque
d.append('last')

# Add 'first' tp the left end of deque
d.appendleft('first')

# Print current deque (convertr to list for display)
print("the deque after adding the elements:", list(d))

# Remove and return element from right end
print("Removed last element:", d.pop())

# Remove and return element from left and 
print("Removed first element:", d.popleft())

# Print the queue after removing the elements
print("The deque after removing certain elements:", list(d))
