import csv
import sqlite3

def save_csv_to_sqlite(csv_filepath, db_filepath):
    with open(csv_filepath) as csv_file:
        reader = csv.DictReader(csv_file)
        next(reader)  # Пропускаем заголовок CSV файла

        with sqlite3.connect(db_filepath) as conn:
            cur = conn.cursor()
            try:
                for row in reader:
                    cur.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", list(row.values()))
            except Exception as e:
                print(f"Ошибка при импорте данных: {e}")
            finally:
                # Проверяем количество добавленных строк
                if len(tuple(reader)) > 0:
                    print(f"{len(tuple(reader))} rows inserted successfully.")
                else:
                    print("No rows were inserted.")
                # Сохраняем изменения в базе данных
                conn.commit()
                # Закрываем соединение с базой данных
                conn.close()
                # закрываем курсор
                cur.close()

if __name__ == "__main__":
    save_csv_to_sqlite('file.csv', 'database.db')