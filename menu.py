class Menu:
    def greeting(self):
        print('Hi user, welcome to my calculator')
    
    def listen(self):
        return input('select an option')

    def exit(self):
        pass


def test():
    m = Menu()
    m.greeting()
    (m.listen())

if __name__ == '__main__':
    test()
