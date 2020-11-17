import sqlite3

conn = sqlite3.connect('carros.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE carro (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        placa TEXT NOT NULL,
        potencia TEXT NOT NULL,
        cor  TEXT NOT NULL
    );
""")

print("Tabela criada.")

cursor.execute("""
    INSERT INTO carro (marca, modelo, placa, potencia, cor)
    VALUES ('FORD', 'KA', 'CARR-0001', '3', 'branco')
""")

cursor.execute("""
    SELECT * FROM carro;
""")

for linha in cursor.fetchall():
    print(linha)



conn.close()