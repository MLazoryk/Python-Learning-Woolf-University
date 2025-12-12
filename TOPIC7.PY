#TASK1
#import collections 

#Person = collections.namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

#person = Person('Maks', 'Lazoryk', 18, 'Lviv', '01146')

#print(person.first_name)
#print(person.last_name)
#print(person.age)
#print(person.birth_place)
#print(person.post_index)



#TASK2
#import collections

#Cat = collections.namedtuple('Cat',['nickname','age','owner'])
#cat = Cat('Mafia', 4, 'Robert')

#print(f"This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}")



#TASK3
student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]

# Empty dictionary to store mark counts
mark_counts = {}

# Loop through each mark in the list
for mark in student_marks:

    # Check if mark already exists in dictionary
    if mark in mark_counts:

        
