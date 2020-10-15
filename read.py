import sqlite3


class Read:
    def count_cart_quantity(self):
        connection = sqlite3.connect('test.db')
        count = connection.execute('SELECT COUNT(*) FROM cart')
        for row in count:
            return row[0]


    def calculate_price(self):
        connection = sqlite3.connect('test.db')
        total_price = connection.execute('SELECT SUM(price) FROM cart')
        for row in total_price:
            return row[0]
