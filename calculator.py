class Calculator:
    def add(self):
        num1 = int(input('Input first number:'))
        num2 = int(input('Input second number:'))

        print('result is', num1 + num2)

    def subtract(self):
        num1 = int(input('Input first number:'))
        num2 = int(input('Input second number:'))

        print('result is', num1 - num2)

    def multiply(self):
        num1 = int(input('Input first number:'))
        num2 = int(input('Input second number:'))

        print('result is', num1 * num2)

    def divide(self):
        num1 = int(input('Input first number:'))
        num2 = int(input('Input second number:'))

        print('result is', num1 // num2)


def test():
    c = Calculator()
    c.multiply()
    
if __name__ == '__main__':
    test()
    