from typing import List
from model import product
from repository import ProductRepositoryImpl, ProductRepository


class ProductController:
    products: List[product.Product] = []

    def __init__(self, repository = ProductRepositoryImpl()):
        self.repository: ProductRepository = repository

    def insertNewProduct(self, name, price, inStock):
        self.repository.insertProduct(
            product=product.Product(name, price, inStock)
        )

    def getAllProducts(self) -> List[product.Product]:
        self.products = self.repository.getAllProducts()

        return self.products

    def serchText(self, search: str) -> List[product.Product]:
        if search == "":
            return self.products
        
        return filter(lambda k: search in k.name, self.products)  # type: ignore

    def removeProduct(self, index: int) -> bool:
        return self.repository.deleteProduct(self.products[index].id)

    def editProduct(self, id: int, product: product.Product) -> bool:
        return self.repository.updateProduct(id, product)
