import sqlite3

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),SECTION VARCHAR(25),MARK INT)
"""

cursor.execute(table_info)


records = [
    ("Yassine", "10A", "A", 95),
    ("Amir", "10B", "B", 88),
    ("Salma", "10A", "A", 92),
]

for rec in records:
    cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARK) VALUES (?, ?, ?, ?)", rec)

data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()

