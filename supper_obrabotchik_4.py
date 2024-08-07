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
sql_path = 'create_table.sql'


# Создаем таблицу для хранения данных
#def create_table():
print(os.path.exists(sql_path))

# with open(sql_path, 'r') as file, sqlite3.connect('database.db') as conn:
#     #print(file.read())
#     conn.executescript(file.read())

def execute_sql_script(sql_path, db_path):
    with open(sql_path, 'r') as file, sqlite3.connect(db_path) as conn:
        conn.executescript(file.read())


def unpack_gz():
    #print(os.listdir(source_dir))
    # Перебираем все файлы в папке
    for file in os.listdir(source_dir):
        # Распаковываем архив
        with gzip.open(os.path.join(source_dir, file), 'rt') as gz:
                #gz.extractall(path=source_dir)
            reader = gz.readlines()
            count = 0
            cur = conn.cursor()
            conn = sqlite3.connect('database.db')

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
                        print(elem)
                        cur.execute("INSERT INTO country VALUES (2, elem[5]) ON DUPLICATE KEY UPDATE contry = elem[5]")
                        cur.execute("INSERT INTO city VALUES (2, elem[6])ON DUPLICATE KEY UPDATE city = elem[6]")
                        #cur.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", list(elem))

                count = count + 1 

        # Сохраняем изменения в базе данных
    conn.commit()
        # закрываем курсор
    #cur.close()
        # Закрываем соединение с базой данных
    conn.close()

# Вызов функции для импорта данных
#save_csv_to_sqlite('file.csv', 'database.db')