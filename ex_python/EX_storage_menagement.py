class Product:
    
    product_count = 0   #variable that keeps track of the number of products, just as the exercise about students
    
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        Product.product_count += 1   #increment the product_count variable by 1
    
    def total_product_worth(self):
        return self.quantity * self.price    #return the total worth of the product it doesn't print it
    
    @staticmethod
    def get_product_count():
        print(f"Total number of products: {Product.product_count}")   #static method that prints the total number of products created
        
product1 = Product("Laptop", 10, 500)
product2 = Product("Smartphone", 20, 300)  #create two products

print(product1.total_product_worth())
print(product2.total_product_worth())

Product.get_product_count()  #call the static method