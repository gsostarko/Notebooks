import sqlite3

conn = sqlite3.connect('hospital.db')

conn.execute("PRAGMA foreign_keys = ON")

conn.execute("INSERT INTO DOCTOR (NAME, PHONE_NUMBER, TYPE)\
    VALUES('John' , '234-98877','Dermatologist')");

conn.execute("INSERT INTO DOCTOR (NAME, PHONE_NUMBER, TYPE)\
    VALUES('Albert' , '234-56585','Cardiologist')");

conn.execute("INSERT INTO PATIENT (NAME, EMAIL_ADRESS, PHONE_NUMBER, PROBLEM , DOCTOR_ID) \
    VALUES('Jack' , 'jack@gmail.com', '512-9834', 'skin burn', 1)");

conn.execute("INSERT INTO PATIENT (NAME, EMAIL_ADRESS, PHONE_NUMBER, PROBLEM , DOCTOR_ID) \
    VALUES('Marko' , 'marko@gmail.com', '512-9834', 'hand burn', 2)");

conn.execute("INSERT INTO PATIENT (NAME, EMAIL_ADRESS, PHONE_NUMBER, PROBLEM , DOCTOR_ID) \
    VALUES('Ivan' , 'ivan@gmail.com', '512-9834', 'leg burn', 2)");

conn.commit()
conn.close()