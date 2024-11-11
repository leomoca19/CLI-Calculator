options = '0 - Exit\n\
1 - add\n\
2 - subtract\n\
3 - multiply\n\
4 - divide\n'

class Menu:
    def greeting(self):
        print('Hi user, welcome to my calculator')
    
    def listen(self):
        return int(input(options + 'Select an option:'))

    def exit(self):
        input('Goodbye user.\nPress enter to exit <Enter>')


def test():
    m = Menu()
    m.greeting()

if __name__ == '__main__':
    test()
