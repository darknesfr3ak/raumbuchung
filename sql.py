import sqlite3  ## SQLite >:( # MYSQL VIEL BESSER >:D

mydb = sqlite3.connect('raumbuchung.db')

if True: # run query
    mydb.execute("CREATE TABLE IF NOT EXISTS room (id INTEGER PRIMARY KEY NOT NULL, name VARCHAR(50))")

mydb.close()




def add_Worker(firstname, lastname):
    mydb = sqlite3.connect('raumbuchung.db')
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO worker (firstname, lastname) VALUES (?, ?)", [firstname, lastname])
    mydb.commit()
    mydb.close()
    return True

#add_Worker("Holger", "Trampe")
    
def remove_Worker(id):
    mydb = sqlite3.connect('raumbuchung.db')
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM worker WHERE id = (?)", [id])
    mydb.commit()
    mydb.close()
    return True

#remove_Worker(1)
    
def get_Worker():
    mydb = sqlite3.connect('raumbuchung.db')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM worker")
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult
    
def add_Room(name):
    mydb = sqlite3.connect('raumbuchung.db')
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO room (name) VALUES (?)", [name])
    mydb.commit()
    mydb.close()
    return True

#add_Room("OG_1_1")

def remove_Room(id):
    mydb = sqlite3.connect('raumbuchung.db')
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM room WHERE id = (?)", [id])
    mydb.commit()
    mydb.close()
    return True

#remove_Room(2)
    
def get_Room():
    mydb = sqlite3.connect('raumbuchung.db')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM room")
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult

def add_Booking(workerId,roomId,date,time):
    mydb = sqlite3.connect('raumbuchung.db')
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO booking (worker, room, date, time) VALUES (?, ?, ?, ?)", [workerId, roomId, date, time])
    mydb.commit()
    mydb.close()
    return True

#add_Booking(1, "randomtime", 1)
    
def remove_Booking(id):
    mydb = sqlite3.connect('raumbuchung.db')
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM booking WHERE id = (?)", [id])
    mydb.commit()
    mydb.close()
    return True

#remove_Booking(1)
    
def get_Booking():
    mydb = sqlite3.connect('raumbuchung.db')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM booking")
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult


