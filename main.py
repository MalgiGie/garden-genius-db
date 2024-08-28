import mysql.connector

# Konfiguracja połączenia z bazą danych
config = {
    'user': 'gosia',        # Zamień na nazwę użytkownika MySQL
    'password': '2367',                # Zamień na hasło MySQL
    'host': 'localhost',                      # Adres serwera MySQL (zwykle localhost)
    'database': 'moja_baza',    # Zamień na nazwę bazy danych
    'port': 3306                              # Port MySQL (zwykle 3306)
}

# Nawiązanie połączenia z bazą danych
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Tworzenie tabeli Gatunek
create_table_query = '''
CREATE TABLE IF NOT EXISTS Gatunek (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nazwa VARCHAR(100) NOT NULL,
    typ ENUM('warzywa', 'zioła') NOT NULL,
    ilosc_wody_ml INT NOT NULL
)
'''
cursor.execute(create_table_query)

# Dodawanie przykładowych danych
insert_data_query = '''
INSERT INTO Gatunek (nazwa, typ, ilosc_wody_ml)
VALUES (%s, %s, %s)
'''
gatunki = [
    ('Bazylia', 'zioła', 500),
    ('Pomidor', 'warzywa', 2000),
    ('Oregano', 'zioła', 300),
    ('Ogórek', 'warzywa', 1500)
]

cursor.executemany(insert_data_query, gatunki)

# Zatwierdzenie transakcji
conn.commit()

# Zamykanie połączenia
cursor.close()
conn.close()

print("Tabela Gatunek została stworzona i wypełniona przykładowymi danymi.")
