Скрипт для загрузки данных из csv файлов в БД

Первая цель задания: это спроектировать схему БД и создать инициализационный sql скрипт для создания всех необходимых таблиц. Смысл создания схемы БД - избежать повторов в данных либо их минимизировать.

Вторая цель: изучить модуль sqllite3 из стандартной библиотеки python.

Скрипт должен принимать следующие аргументы:

-f --files список имен файлов для обработки

-d --database путь к файлу БД sqlite3 (куда записывать данные)

Скрипт должен делать:

В случае если файла с БД не существует создавать его

Создавать схему БД если таковая отсуствует

Вставлять данные согласно схеме БД в соответствующие таблицы

Задача дожна быть оформлена в виде репозитория на GitHub# DEVOPS_3-
