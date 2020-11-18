import sqlite3

conn = sqlite3.connect('veiculos.db')

cursor = conn.cursor()

cursor.execute("""
    INSERT INTO veiculo (tipo, marca, modelo, placa, potencia, cor, proprietario, qtd_passageiros, motor, combustivel, ano, nome, num_rodas, meio_locomocao)
    VALUES ('CARRO', 'RENAULT', 'CAPTUR', 'CARR-0011', '2', 'bege', 'Eduarda', '4', 'motor', 'gasolina', '2020', 'relâmpago mcqueen', 4, 'terrestre')
""")

cursor.execute("""
    INSERT INTO veiculo (tipo, marca, modelo, placa, potencia, cor, proprietario, qtd_passageiros, motor, combustivel, ano, nome, num_rodas, meio_locomocao)
    VALUES ('CARRO', 'RENAULT', 'SANDERO', 'CARR-0012', '1', 'preto', 'Eduarda', '4', 'motor', 'gasolina', '2020', 'relâmpago mcqueen', 4, 'terrestre')
""")

cursor.execute("""
    INSERT INTO veiculo (tipo, marca, modelo, placa, potencia, cor, proprietario, qtd_passageiros, motor, combustivel, ano, nome, num_rodas, meio_locomocao)
    VALUES ('CARRO', 'RENAULT', 'CAPTUR', 'CARR-0013', '2', 'bege', 'Eduarda', '4', 'motor', 'gasolina', '2020', 'relâmpago mcqueen', 4, 'terrestre')
""")

cursor.execute("""
    INSERT INTO veiculo (tipo, marca, modelo, placa, potencia, cor, proprietario, qtd_passageiros, motor, combustivel, ano, nome, num_rodas, meio_locomocao)
    VALUES ('CARRO', 'FORD', 'FIESTA', 'CARR-0013', '2', 'branco', 'Eduarda', '4', 'motor', 'gasolina', '2019', 'relâmpago mcqueen', 4, 'terrestre')
""")

cursor.execute("""
    INSERT INTO veiculo (tipo, marca, modelo, placa, potencia, cor, proprietario, qtd_passageiros, motor, combustivel, ano, nome, num_rodas, meio_locomocao)
    VALUES ('CARRO', 'FORD', 'KA', 'CARR-0014', '2', 'branco', 'Carlito', '4', 'motor', 'gasolina', '2020', 'relâmpago mcqueen', 4, 'terrestre')
""")

cursor.execute("""
    UPDATE veiculo 
    SET placa = 'CAR-0015' 
    WHERE id = 5""")

conn.commit()

conn.close()