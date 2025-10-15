''' new_dict = {new_key:new_value for (key, value) in dict.items() if condition}'''
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student: score for student,
                   score in students_scores.items() if int(score) >= 30}
print(passed_students)
