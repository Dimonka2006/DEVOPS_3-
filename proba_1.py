import os
import gzip
import sqlite3
import csv

# Путь к папке с архивами
source_dir = 'archive'
#print(os.path.exists(source_dir))
#print(os.listdir(source_dir))
# Путь к базе данных
db_path = 'database.db'

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
                    print(elem)
                    #cur.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", list(elem))
            count = count + 1 

        # Сохраняем изменения в базе данных
        #conn.commit()
        # закрываем курсор
        #cur.close()
        # Закрываем соединение с базой данных
        #conn.close()

