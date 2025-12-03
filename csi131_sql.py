'''
script: cis131_lab_sql.py
action: This script is a demonstration of the SQL library.
Author: Declan Juliano
Date:   12/2/2025
'''

import sqlite3

# connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# load schema and data from the provided SQL file
with open("books.sql", "r") as f:
    sql_script = f.read()
cursor.executescript(sql_script)
conn.commit()


# print all authors last names in decending order
print("All Authors' Last Names in Descending Order:")
cursor.execute("SELECT last FROM authors ORDER BY last DESC")
for row in cursor.fetchall():
    print(row[0])


# print all titles in ascending order
print("\nAll Titles in Ascending Order:")
cursor.execute("SELECT title FROM titles ORDER BY title ASC")
for row in cursor.fetchall():
    print(row[0])



# use inner join to select all books for a specific author
print("\nInner join results for books by Paul Deitel:")
cursor.execute("""
    SELECT titles.title, titles.copyright, titles.isbn
    FROM authors
    INNER JOIN author_ISBN ON authors.id = author_ISBN.id
    INNER JOIN titles ON author_ISBN.isbn = titles.isbn
    WHERE authors.first = 'Paul' AND authors.last = 'Deitel'
    ORDER BY titles.title ASC
""")
for row in cursor.fetchall():
    print(row)


# insert a new author
print("\nInserting new author Grace Hopper:")
cursor.execute("INSERT INTO authors (first, last) VALUES (?, ?)", ("Grace", "Hopper"))
conn.commit()

# confirm insertion
cursor.execute("SELECT * FROM authors WHERE first = 'Grace' AND last = 'Hopper'")
print(cursor.fetchone())


# insert a new title for author
print("\nInserting new title for Grace Hopper:")
# step 1: Insert into titles
cursor.execute("""
    INSERT INTO titles (isbn, title, edition, copyright)
    VALUES (?, ?, ?, ?)
""", ("9999999999", "Programming Pioneers", 1, "2025"))

# step 2: Get Grace Hopper's ID
cursor.execute("SELECT id FROM authors WHERE first = 'Grace' AND last = 'Hopper'")
grace_id = cursor.fetchone()[0]

# step 3: Insert into author_ISBN
cursor.execute("INSERT INTO author_ISBN (id, isbn) VALUES (?, ?)", (grace_id, "9999999999"))
conn.commit()

# confirm insertion
cursor.execute("""
    SELECT titles.title, authors.first, authors.last
    FROM titles
    JOIN author_ISBN ON titles.isbn = author_ISBN.isbn
    JOIN authors ON author_ISBN.id = authors.id
    WHERE titles.isbn = '9999999999'
""")
print(cursor.fetchone())