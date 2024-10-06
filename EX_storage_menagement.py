class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def total_product_worth(self):
        return self.quantity * self.price
    
spugna = Product("Spugna", 10, 2)
print(spugna.total_product_worth())