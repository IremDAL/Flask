import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Sorular tablosu
cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL,
    correct_option TEXT NOT NULL
)
""")

# Skorlar tablosu
cursor.execute("""
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    score INTEGER NOT NULL
)
""")

# Örnek sorular
questions = [
    ("Discord botu oluşturmak için hangi kütüphane yaygın olarak kullanılır?", "Flask", "TensorFlow", "Discord.py", "NLTK", "option3"),
    ("Python ile web geliştirmek için en çok kullanılan framework nedir?", "Flask", "OpenCV", "PyTorch", "NLTK", "option1"),
    ("Hangisi yapay zeka geliştirme kütüphanesidir?", "TensorFlow", "Flask", "Discord.py", "BeautifulSoup", "option1"),
    ("Bilgisayarla görme için hangi kütüphane uygundur?", "ImageAI", "BeautifulSoup", "Flask", "NLTK", "option1"),
    ("Doğal dil işleme için hangi kütüphane uygundur?", "TensorFlow", "Discord.py", "NLTK", "Flask", "option3")
]

cursor.executemany("""
INSERT INTO questions (question, option1, option2, option3, option4, correct_option)
VALUES (?, ?, ?, ?, ?, ?)
""", questions)

conn.commit()
conn.close()
print("Veritabanı oluşturuldu ve örnek sorular eklendi ✅")
