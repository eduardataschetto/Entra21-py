import sqlite3

conn = sqlite3.connect('veiculos.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE veiculo (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        tipo TEXT,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        placa TEXT NOT NULL,
        potencia TEXT NOT NULL,
        cor  TEXT NOT NULL
    );
""")

print("Tabela criada.")

conn.close()