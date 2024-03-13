import sqlite3
from faker import Faker
import random

conn = sqlite3.connect('homework.db')

cur = conn.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        book_name TEXT NOT NULL,
        num_of_pages INTEGER,
        first_page_type TEXT,
        category TEXT
    );
'''
cur.execute(create_table)

fake = Faker()
for _ in range(10):
    book_name = fake.catch_phrase()
    pages = random.randint(50, 500)
    first_page_type = random.choice(['Text', 'Image'])
    category = fake.word()

    cur.execute("INSERT INTO books (book_name, num_of_pages, first_page_type, category) VALUES (?, ?, ?, ?)",
                (book_name, pages, first_page_type, category))

cur.execute("SELECT AVG(num_of_pages) FROM books")
result = cur.fetchone()[0]

cur.execute("SELECT book_name FROM books WHERE num_of_pages = (SELECT MAX(num_of_pages) FROM books)")
result1 = cur.fetchone()

conn.commit()
conn.close()

print("Table 'books' created successfully.")
print("10 random books added to the 'books' table.")
print(f"Average number of pages: {result:.2f}")
print(f"The book with the highest number of pages is: {result1[0]}")