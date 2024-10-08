import sqlite3
import csv

def save_csv_to_sqlite(csv_filepath, db_filepath):
    # Открытие файла CSV
    with open(csv_filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        # Создание подключения к базе данных
        conn = sqlite3.connect(db_filepath)
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


        # Вставка данных из CSV в базу данных
        for row in reader:
            values = []
            for key in row:
                values.append("'" + str(row[key]) + "'")
            sql = "INSERT INTO users VALUES (" + ",".join(values) + ")"
            cur.execute(sql)
        # Сохраняем изменения в базе данных
        conn.commit()
        # Закрываем соединение с базой данных
        conn.close()

# Вызов функции для импорта данных
save_csv_to_sqlite('file.csv', 'database.db')