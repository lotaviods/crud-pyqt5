class Product():
    id: int
    name: str
    price: str
    stock: str

    def __init__(self, name: str, price: str, stock: str, id: int = None) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        pass

    def __str__(self) -> str:
        return f"{self.name} | price: {self.price} | stock: {self.stock}"