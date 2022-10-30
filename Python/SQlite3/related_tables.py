import sqlite3

conn = sqlite3.connect('hospital.db')

q1 = ('''CREATE TABLE IF NOT EXISTS DOCTOR
        (ID INTEGER PRIMARY KEY,
        NAME TEXT NOT NULL,
        PHONE_NUMBER CHAR(20) NOT NULL,
        TYPE TEXT); ''')

conn.execute(q1)

q2 = (''' CREATE TABLE IF NOT EXISTS PATIENT
        (ID INTEGER PRIMARY KEY,
        NAME TEXT NOT NULL,
        EMAIL_ADRESS TEXT NOT NULL,
        PHONE_NUMBER CHAR(20) NOT NULL,
        PROBLEM TEXT,
        DOCTOR_ID INTEGER NOT NULL,
        FOREIGN KEY(DOCTOR_ID) REFERENCES DOCTOR(ID));''')

conn.execute(q2)
conn.close()
