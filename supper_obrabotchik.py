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
        cur.execute('''CREATE TABLE IF NOT EXISTS table (
            name TEXT,
            birth INTEGER,
            job TEXT,
            company TEXT,
            country TEXT,
            city TEXT,
            address TEXT,
            zip_code INTEGER,                                         
            phone INTEGER,
            email TEXT,
            card_number INTEGER,
            card_expire INTEGER,
            security_code INTEGER,
            url TEXT
        )''')
        # name;birth;job;company;country;city;address;zip_code;phone;
        # email;card_number;card_expire;security_code;url

        # Проходим по каждой строке CSV файла и записываем данные в таблицу
        next(reader)  # Пропускаем заголовок CSV файла
        for row in reader:
            cur.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)
        # Сохраняем изменения в базе данных
        conn.commit()
        # Закрываем соединение с базой данных
        conn.close()
save_csv_to_sqlite('data.csv', 'data.db')