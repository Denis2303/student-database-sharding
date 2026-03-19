from pymongo import MongoClient

class StudentApp:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client.universityDB
        self.students = self.db.students
    
    def menu(self):
        while True:
            print('\n1. Все студенты')
            print('2. Найти по ID')
            print('3. Добавить студента')
            print('4. Статистика')
            print('5. Инфо о шардинге')
            print('0. Выход')
            
            choice = input('Выберите: ')
            
            if choice == '1':
                for s in self.students.find().limit(10):
                    print(f"{s['student_id']} - {s['name']} - {s['faculty']}")
            
            elif choice == '2':
                sid = int(input('ID: '))
                s = self.students.find_one({'student_id': sid})
                if s:
                    print(f"ID: {s['student_id']}")
                    print(f"Имя: {s['name']}")
                    print(f"Факультет: {s['faculty']}")
                    print(f"Курс: {s['course']}")
                    print(f"Статус: {s['status']}")
            
            elif choice == '3':
                s = {
                    'student_id': int(input('ID: ')),
                    'name': input('Имя: '),
                    'faculty': input('Факультет: '),
                    'course': int(input('Курс: ')),
                    'group': input('Группа: '),
                    'status': input('Статус: ')
                }
                self.students.insert_one(s)
                print('Добавлено')
            
            elif choice == '4':
                stats = self.students.aggregate([
                    {'$group': {'_id': '$faculty', 'count': {'$sum': 1}}}
                ])
                for s in stats:
                    print(f"{s['_id']}: {s['count']}")
            
            elif choice == '5':
                shards = self.client.admin.command('listShards')
                print(f"Шардов: {len(shards['shards'])}")
                for s in shards['shards']:
                    print(f"  {s['_id']}")
            
            elif choice == '0':
                break

if __name__ == '__main__':
    app = StudentApp()
    app.menu()