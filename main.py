from menu import Menu
from calculator import Calculator

m = Menu()
m.greeting()

while m.listen() != 0:
    print('Listening...')

m.exit()