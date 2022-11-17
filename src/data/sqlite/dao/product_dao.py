import sqlite3
from typing import List

from model.product import Product


class ProductDAO:
    connection: sqlite3.Connection

    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection
        self.__createTableIfNotExist()
        pass

    def __createTableIfNotExist(self):
        cursor = self.connection.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS product(id INTEGER PRIMARY KEY, name TEXT, price INTEGER, stock INTEGER)')
        cursor.close()

    def insertProduct(self, product: Product) -> bool:
        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO product(name, price, stock) VALUES(?, ?, ?)", (
            product.name, product.price, product.stock))
        self.connection.commit()
        rowCount = cursor.rowcount

        self.connection.commit()
        cursor.close()

        return True if rowCount == 1 else False

    def queryProduct(self, id: int) -> Product:
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM product WHERE id=?", (id,))

        row = cursor.fetchone()
        self.connection.commit()

        cursor.close()
        if (row == None):
            return None

        return Product(row[1], row[2], row[3], row[0])

    def updateProduct(self, id: int, newProduct: Product) -> bool:
        cursor = self.connection.cursor()

        cursor.execute(
            "UPDATE product SET name = ?, price = ?, stock = ? WHERE id = ?", 
            (newProduct.name, newProduct.price, newProduct.stock, id))

        self.connection.commit()
        cursor.close()

        return True if cursor.rowcount == 1 else False

    def deleteProduct(self, id: int) -> bool:
        cursor = self.connection.cursor()

        cursor.execute("DELETE FROM product WHERE id=?", (id, ))
        self.connection.commit()
        rowCount = cursor.rowcount

        self.connection.commit()
        cursor.close()

        return True if rowCount == 1 else False

    def getAllProducts(self) -> List[Product]:
        cursor = self.connection.cursor()
        
        cursor.execute("SELECT * FROM product")
        self.connection.commit()
        result = cursor.fetchall()
        products = []
        for i in result:
            products.append(Product(i[1], i[2], i[3], i[0]))  
        return products