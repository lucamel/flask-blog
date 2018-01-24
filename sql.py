import sqlite3

with sqlite3.connect('blog.db') as connection:
    c = connection.cursor()

    c.execute('CREATE TABLE posts (title TEXT, post TEXT)')

    posts = [
        ('Good', 'I\'m good!'),
        ('Well', 'I\'m well!'),
        ('Excelent', 'I\'m excelent!'),
        ('Okay', 'I\'m okay!')
    ]

    c.executemany('INSERT INTO posts VALUES(?, ?)', posts)
    