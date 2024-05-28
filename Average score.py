# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# grades = [[(5 + 3 + 3 + 5 + 4)//5], [(2 + 2 + 2 + 3)//4], [(4 + 5 + 5 + 2)//4], [(4 + 4 + 3)//3], [(5 + 5 + 5 + 4 + 5)//5]]
grades = [[(5 + 3 + 3 + 5 + 4)/5], [(2 + 2 + 2 + 3)/4], [(4 + 5 + 5 + 2)/4], [(4 + 4 + 3)/3], [(5 + 5 + 5 + 4 + 5)/5]]
print(grades)
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # Во множестве происходит движение, туса
print(students)
new_students = list(students) # А список это всю пати стабилизирует
print(new_students)
new_students.sort() # Упорядочивает в алфавитном порядке
dict = {} # Создаём словарь
print(new_students)
dict = {new_students[0]: grades[0], new_students[1]: grades[1], new_students[2]: grades[2], new_students[3]: grades[3], new_students[4]: grades[4]}
print(dict) 