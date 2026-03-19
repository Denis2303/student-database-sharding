from pymongo import MongoClient
import random
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client.universityDB
collection = db.students

faculties = ['ФКН', 'ФЭН', 'МИЭФ', 'ФМ', 'ФБ', 'МШЭ']
statuses = ['учится', 'академический отпуск', 'выпустился']

students = []
for i in range(1, 10001):
    student = {
        'student_id': i,
        'name': f'Студент_{i}',
        'faculty': random.choice(faculties),
        'course': random.randint(1, 4),
        'group': f'{random.randint(1, 20)}{random.choice(["А","Б","В"])}',
        'status': random.choice(statuses),
        'enrollment_date': datetime.now()
    }
    students.append(student)
    
    if len(students) == 1000:
        collection.insert_many(students)
        students = []

if students:
    collection.insert_many(students)