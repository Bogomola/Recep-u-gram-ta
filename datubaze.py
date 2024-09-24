import sqlite3

conn = sqlite3.connect('recepsu_gramata.db')
cursor = conn.cursor()

# Izveido tabulu Kategorijas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Kategorijas (
    KategorijasID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nosaukums TEXT NOT NULL
)
''')

# Izveido tabulu Receptes
cursor.execute('''
CREATE TABLE IF NOT EXISTS Receptes (
    ReceptesID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nosaukums TEXT NOT NULL,
    KategorijasID INTEGER,
    FOREIGN KEY (KategorijasID) REFERENCES Kategorijas(KategorijasID)
)
''')

# Izveido tabulu priekšv Sastāvdaļas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Sastavdalas (
    SastavdalaID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nosaukums TEXT NOT NULL
)
''')

# Izveido relāciju tabulu Daudzums
cursor.execute('''
CREATE TABLE IF NOT EXISTS Daudzums (
    ReceptesID INTEGER,
    SastavdalaID INTEGER,
    Daudzums FLOAT NOT NULL,
    Mervienibas TEXT NOT NULL,
    PRIMARY KEY (ReceptesID, SastavdalaID),
    FOREIGN KEY (ReceptesID) REFERENCES Receptes(ReceptesID),
    FOREIGN KEY (SastavdalaID) REFERENCES Sastavdalas(SastavdalaID)
)
''')

# Saglabā izmaiņas un aizver savienojumu
conn.commit()
conn.close()

print("Datubāze un tabulas ir veiksmīgi izveidotas!")
