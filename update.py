import sqlite3


class Update:
    def update_cart_value(self):
        connection = sqlite3.connect('test.db')
        id = input("Enter the id that you want to change")
        name = input("Enter the name to update")
        price = input("Enter the price")

        query = "Update cart Set Name = ?, price =? Where Id =?"

        connection.execute(query, [name, price, id])
        connection.commit()
        print("Item updated successfully")
