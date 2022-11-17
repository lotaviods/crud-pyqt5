import abc
from typing import List
from model.product import Product


class ProductRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insertProduct(self, product: Product) -> bool:
        raise NotImplementedError
    
    @abc.abstractmethod
    def getProductById(self, id: int) -> Product:
        raise NotImplementedError

    @abc.abstractmethod
    def getAllProducts(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def updateProduct(self, id: int, newProduct: Product) -> bool: 
        raise NotImplementedError

    @abc.abstractmethod
    def deleteProduct(self, id: int) -> bool:
        raise NotImplementedError
    