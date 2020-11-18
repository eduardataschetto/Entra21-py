import sqlite3

conn = sqlite3.connect('veiculos.db')
cursor = conn.cursor()

cursor.execute("""
ALTER TABLE veiculo
ADD COLUMN proprietario TEXT;
""")

cursor.execute("""
ALTER TABLE veiculo
ADD COLUMN qtd_passageiros INTEGER;
""")

cursor.execute("""
ALTER TABLE veiculo
ADD COLUMN motor TEXT;
""")

cursor.execute("""
ALTER TABLE veiculo
ADD COLUMN combustivel TEXT;
""")

cursor.execute("""
ALTER TABLE veiculo
ADD COLUMN ano TEXT;
""")

cursor.execute("""
ALTER TABLE veiculo
ADD COLUMN nome TEXT;
""")

cursor.execute("""
ALTER TABLE veiculo
ADD COLUMN num_rodas INTEGER;
""")

cursor.execute("""
ALTER TABLE veiculo
ADD COLUMN meio_locomocao TEXT;
""")

conn.commit()