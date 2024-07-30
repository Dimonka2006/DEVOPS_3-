import sqlite3
import csv
import os
import tarfile

# Путь к папке с архивами
source_dir = 'path/to/your/directory'

# Путь к базе данных
db_path = 'path/to/your/database.db'

# Перебираем все файлы в папке
for file in os.listdir(source_dir):
    # Распаковываем архив
    with tarfile.open(os.path.join(source_dir, file), 'r:gz') as tar:
        tar.extractall(path=source_dir)

    # Перебираем все CSV файлы
    for csv_file in os.listdir(source_dir):
        if csv_file.endswith('.csv'):
            # Открываем CSV файл
            with open(os.path.join(source_dir, csv_file)) as f:
                # Читаем данные из CSV файла
                csv_data = f.read()


def save_csv_to_sqlite(csv_filepath, db_path):
    # Открытие файла CSV
    with open(csv_filepath, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        # Создание подключения к базе данных
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        # Создаем таблицу для хранения данных
        cur.execute('''CREATE TABLE IF NOT EXISTS users(
            name TEXT,
            birth TEXT,
            job TEXT,
            company TEXT,
            country TEXT,
            city TEXT,
            address TEXT,
            zip_code TEXT,                                         
            phone TEXT,
            email TEXT,
            card_number TEXT,
            card_expire TEXT,
            security_code TEXT,
            url TEXT
        )''')
        # name;birth;job;company;country;city;address;zip_code;phone;
        # email;card_number;card_expire;security_code;url
        
        # Проходим по каждой строке CSV файла и записываем данные в таблицу
        next(reader)  # Пропускаем заголовок CSV файла
        count = 1
        for row in reader:
            if count %2 != 0:
                row1 = row
            else:
                row1 = row1 + row
                #print(row1)       
                st = ''.join(row1) 
                elem = st.split(';') # 
                #print(elem)
                cur.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", list(elem))
            count = count + 1 

        # Сохраняем изменения в базе данных
        conn.commit()
        # закрываем курсор
        cur.close()
        # Закрываем соединение с базой данных
        conn.close()

# Вызов функции для импорта данных
save_csv_to_sqlite('file.csv', 'database.db')