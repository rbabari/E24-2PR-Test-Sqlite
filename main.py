# importer sqlite
import sqlite3
# se connecter
connection = sqlite3.connect('test.db')
# on créer un objet cursor. cet ovjet permet d'envoyer des requetes
cursor = connection.cursor()

# creéer une table si cela n'existe pas ...
#cursor.execute("CREATE TABLE Persons (PersonID int,LastName varchar(255),FirstName varchar(255),City varchar(255))")

# Faire des requetes


cursor.execute("INSERT INTO Persons (PersonID, LastName, FirstName, City) VALUES (3, 'samiha', 'mecheri', 'montreal');")

cursor.execute("SELECT * FROM Persons;")

# delete from Persons WHERE PersonID = 3;

data = cursor.fetchall()
print(data)

connection.commit()
connection.close()