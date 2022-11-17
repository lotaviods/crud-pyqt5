import sqlite3
import unittest
from data import ProductDAO
from model.product import Product


class TestDAOProduct(unittest.TestCase):
    conn: sqlite3.Connection

    def setUp(self):
        self.conn = sqlite3.connect(':memory:')

    def tearDown(self):
        self.conn.close()

    def test_should_create_product(self):
        dao = ProductDAO(self.conn)

        name = "test"
        price = 10
        stock = 10

        dao.insertProduct(product=Product(name, price, stock))

        cursor = self.conn.cursor()
        cursor.execute("select * from product")
        product = cursor.fetchone()

        self.assertEqual(product[0], 1)
        self.assertEqual(product[1], name)
        self.assertEqual(product[2], price)
        self.assertEqual(product[3], stock)

    def test_should_read_product(self):
        dao = ProductDAO(self.conn)
        name = "test"
        price = 10
        stock = 15
        cursor = self.conn.cursor()

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS product(id INTEGER PRIMARY KEY, name TEXT, price INTEGER, stock INTEGER)')
        
        cursor.execute("INSERT INTO product(name, price, stock) VALUES(?, ?, ?)", (
            name, price, stock))
        self.conn.commit()
        
        cursor.close()

        product = dao.queryProduct(1)
        
        self.assertEqual(product.id, 1)
        self.assertEqual(product.name, name)
        self.assertEqual(product.price, price)
        self.assertEqual(product.stock, stock)

    def test_should_update_product(self):
        dao = ProductDAO(self.conn)
        name = "test"
        price = 10
        stock = 15
        cursor = self.conn.cursor()

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS product(id INTEGER PRIMARY KEY, name TEXT, price INTEGER, stock INTEGER)')
        
        cursor.execute("INSERT INTO product(name, price, stock) VALUES(?, ?, ?)", (
            name, price, stock))
        self.conn.commit()
        
        cursor.close()
        
        newName = "newProduct"
        newPrice = 15
        newStock = 20
        newProduct = dao.updateProduct(1, Product(newName, newPrice, newStock, 1))

        cursor = self.conn.cursor()
        cursor.execute("select * from product")
        product = cursor.fetchone()
        
        self.assertEqual(newProduct, True)
        self.assertEqual(product[1], newName)
        self.assertEqual(product[2], newPrice)
        self.assertEqual(product[3], newStock)

    def test_should_delete_product(self):
        dao = ProductDAO(self.conn)
        name = "test"
        price = 10
        stock = 15
        cursor = self.conn.cursor()

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS product(id INTEGER PRIMARY KEY, name TEXT, price INTEGER, stock INTEGER)')
        
        cursor.execute("INSERT INTO product(name, price, stock) VALUES(?, ?, ?)", (
            name, price, stock))
        self.conn.commit()

        result = dao.deleteProduct(1)

        cursor = self.conn.cursor()
        cursor.execute("select * from product")
        product = cursor.fetchone()

        self.assertEqual(result, True)
        self.assertEqual(product, None)

    def test_should_give_product_list(self):
        dao = ProductDAO(self.conn)
        name = "test"
        price = 10
        stock = 15
        cursor = self.conn.cursor()

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS product(id INTEGER PRIMARY KEY, name TEXT, price INTEGER, stock INTEGER)')
        
        cursor.execute("INSERT INTO product(name, price, stock) VALUES(?, ?, ?)", (
            name, price, stock))
        self.conn.commit()

        name2 = "test2"
        price2 = 15
        stock2= 20
        cursor = self.conn.cursor()

        cursor.execute("INSERT INTO product(name, price, stock) VALUES(?, ?, ?)", (
            name2, price2, stock2))

        self.conn.commit()
        result = dao.getAllProducts()

        self.assertEqual(result[0].name, name)
        self.assertEqual(result[0].price, price)
        self.assertEqual(result[0].stock, stock)
        self.assertEqual(result[0].id, 1)

        self.assertEqual(result[1].name, name2)
        self.assertEqual(result[1].price, price2)
        self.assertEqual(result[1].stock, stock2)
        self.assertEqual(result[1].id, 2)

if __name__ == '__main__':
    unittest.main()
