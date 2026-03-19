\# Шардированная БД студентов. Выполнил Томахин Денис



\## Схема БД

\- student\_id (ключ шардирования)

\- name

\- faculty

\- course

\- group

\- status



\## Шардинг

\- 3 шарда по 2 узла

\- Ключ: student\_id (hashed)

\- Настройка через Python



\## Интерфейс

Консольное приложение с CRUD операциями

## Запуск проекта
```bash
docker-compose up -d
pip install -r requirements.txt
python setup_sharding.py
python generate_data.py
python student_app.py
