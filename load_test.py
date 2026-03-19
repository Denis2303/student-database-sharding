from pymongo import MongoClient
import time
import random
import matplotlib.pyplot as plt

client = MongoClient('mongodb://localhost:27017/')
db = client.universityDB
students = db.students

times = []

print('Тестирование чтения...')
for _ in range(100):
    sid = random.randint(1, 10000)
    start = time.time()
    students.find_one({'student_id': sid})
    times.append((time.time() - start) * 1000)

print(f'Среднее время: {sum(times)/len(times):.2f} мс')

plt.hist(times, bins=20)
plt.title('Время выполнения запросов')
plt.xlabel('мс')
plt.ylabel('частота')
plt.savefig('test_result.png')
plt.show()