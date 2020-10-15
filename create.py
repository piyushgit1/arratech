import sqlite3


class Create:
    def Add_to_cart(self):

    # connector=sqlite3.connect('test.db')
        connection = sqlite3.connect('test.db')
        command = "CREATE TABLE IF NOT EXISTS cart(Id INT PRIMARY KEY ,name text NOT NULL,price int NOT NULL)"
        connection.execute(command)

        name = input('Enter Name = ')
        price = input('Enter price = ')

        try:
            query = "Insert Into cart(name, price) Values(?,?)"
            connection.execute(query, [name, price])
            connection.commit()
            print('Item Saved Successfully')

        except:
            print('Something wrong, please check')

        finally:
            connection.close()
