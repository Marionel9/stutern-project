import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

#title and pages are columns and books is the table name
c.execute('''CREATE TABLE IF NOT EXISTS books 
            (title TEXT, pages INTEGER)''')