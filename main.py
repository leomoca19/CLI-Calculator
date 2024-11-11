from menu import Menu
from calculator import Calculator

m = Menu()
c = Calculator()
m.greeting()

while (answer := m.listen()) != 0:  # bug - answer is always 1 because it is boolean
    match answer:
        case 1:
            c.add()
        case 2:
            c.subtract()
        case 3:
            c.multiply()
        case 4:
            c.divide()

m.exit()