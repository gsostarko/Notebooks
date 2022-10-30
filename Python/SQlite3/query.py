import sqlite3

conn = sqlite3.connect('hospital.db')

conn.execute("PRAGMA foreign_keys = ON ")

cursor = conn.execute("SELECT NAME, EMAIL_ADRESS, DOCTOR_ID FROM PATIENT WHERE DOCTOR_ID =1")

for row in cursor:
    print(row)

conn.close()