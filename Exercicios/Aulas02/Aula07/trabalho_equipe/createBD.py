import sqlite3

conn = sqlite3.connect('concessionaria.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE veiculos (
        id_veiculo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        ano TEXT NOT NULL,
        placa TEXT NOT NULL,
        proprietario TEXT NOT NULL,
        num_portas TEXT NOT NULL,
        cor TEXT NOT NULL,
        km_rodado TEXT NOT NULL,
        qtd_passageiros TEXT NOT NULL,
        motor TEXT NOT NULL,
        combustivel TEXT NOT NULL,
        meio_locomocao TEXT NOT NULL,
        valor REAL NOT NULL
    );
""")

cursor.execute("""
    CREATE TABLE pessoas (
        id_pesso INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data_nasc DATE NOT NULL,
        cpf TEXT NOT NULL,
        endereco TEXT NOT NULL,
        salario REAL NOT NULL,
        profissao TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        nome_resp TEXT NOT NULL,
        sexo TEXT NOT NULL,
        naturalidade TEXT NOT NULL,
        nacionalidade TEXT NOT NULL
    );
""")

conn.close()

