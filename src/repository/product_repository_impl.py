import sqlite3
from typing import List
from constants.connection import DATABASE_SQLITE_PATH
from data import ProductDAO
from model.product import Product
from repository.product_repository import ProductRepository

class ProductRepositoryImpl(ProductRepository):
    dao: ProductDAO

    def __init__(self) -> None:
        self.dao = ProductDAO(connection=sqlite3.connect(DATABASE_SQLITE_PATH))
        super().__init__()

    def insertProduct(self, product: Product) -> bool:
        return self.dao.insertProduct(product)

    def getProductById(self, id: int) -> Product:
        return self.dao.queryProduct(id)

    def updateProduct(self, id: int, newProduct: Product) -> bool:
        return self.dao.updateProduct(id, newProduct)

    def deleteProduct(self, id: int) -> bool:
        return self.dao.deleteProduct(id)

    def getAllProducts(self) -> List[Product]:
        return self.dao.getAllProducts()
