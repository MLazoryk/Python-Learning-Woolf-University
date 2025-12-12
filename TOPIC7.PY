# імпортуємо модуль collections для використання namedtuple
import collection

# сторюємо іменований кортеж Person із зазначеними полями
Person = collections.namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

# Створюємо екземпляр Person з конкретними значеннями 
person = Person('Mick', 'Nitch', 35, 'Boston', '01146')
