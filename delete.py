import sqlite3


class delete:
    def delt(self):
        connection = sqlite3.connect('test.db')
        deletequery = "SELECT * FROM cart WHERE Id=?"
        Id = input("input the id to delete")
        connection.execute(deletequery, [Id])
        connection.commit()
        print("Data Deleted Succesfully")
