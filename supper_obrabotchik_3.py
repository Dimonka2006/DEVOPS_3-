import sqlite3
import csv
import os
import gzip

# Путь к папке с архивами
source_dir = 'archive'
#print(os.path.exists(source_dir))
#print(os.listdir(source_dir))
# Путь к базе данных
db_path = 'database.db'

# Создание подключения к базе данных
conn = sqlite3.connect(db_path)
cur = conn.cursor()
# Создаем таблицу для хранения данных
#def create_table():
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



#def unpack_gz():
#print(os.listdir(source_dir))
# Перебираем все файлы в папке
for file in os.listdir(source_dir):
    # Распаковываем архив
    with gzip.open(os.path.join(source_dir, file), 'rt') as gz:
            #gz.extractall(path=source_dir)
        reader = gz.readlines()
        count = 0

        for row in reader:  
            #print(row)
            if count > 0:
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
#save_csv_to_sqlite('file.csv', 'database.db')