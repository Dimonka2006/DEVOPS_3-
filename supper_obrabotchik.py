import sqlite3
import csv

def save_csv_to_sqlite(csv_filepath, db_filepath):
    # Открытие файла CSV
    with open(csv_filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
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

        # Проходим по каждой строке CSV файла и записываем данные в таблицу
        # next(reader)  # Пропускаем заголовок CSV файла
        # for row in reader:
        #     cur.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", tuple(row))
        # # Проверяем количество добавленных строк
        # if cur.rowcount != 0:
        #     print(f"{cur.rowcount} rows inserted successfully.")
        # else:
        #     print("No rows were inserted.")
        # # Сохраняем изменения в базе данных
        # conn.commit()
        # # Закрываем соединение с базой данных
        # conn.close()
        # # Не забываем закрыть курсор
        # cur.close()

#save_csv_to_sqlite('file.csv', 'db/database.db')
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
save_csv_to_sqlite('file.csv', 'db/database.db')