import sqlite3

conn = sqlite3.connect('concessionaria.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT * FROM pessoas
""")


print(cursor.fetchall())

conn.close()