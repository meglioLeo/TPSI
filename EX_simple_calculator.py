class Calculator:
    
    @staticmethod
    def add(x, y):     
        print (x + y)    #print the sum of x and y without needing to create an instance of the class
    
    @staticmethod
    def subtract(x, y):
        print (x - y)   #does the same for subtraction and every other method
    
    @staticmethod
    def multiply(x, y):
        print (x * y)
    
    @staticmethod
    def divide(x, y):
        print (x / y)
    
number1 = 10        #two numbers to be used in the calculations that are not neccessary
number2 = 5
Calculator.add(number1, number2)
Calculator.subtract(number1, number2)
Calculator.multiply(number1, number2)
Calculator.divide(number1, number2)