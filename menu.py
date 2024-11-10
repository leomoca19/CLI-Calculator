class Menu:
    def greeting(self):
        print('Hi user, welcome to my calculator')
    
    def listen(self):
        return input('select an option:')

    def exit(self):
        input('Goodbye user.\nPress enter to exit <Enter>')


def test():
    m = Menu()
    m.greeting()
    (m.listen())

if __name__ == '__main__':
    test()
