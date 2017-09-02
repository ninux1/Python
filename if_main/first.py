#!/usr/bin/env python


class Display:
    def __init__(self, name):
        self.a = 20
        self.b = 30
        print("Name = {}".format(name))

    def run(self):
        print("The Sum is {}".format(self.a+self.b))

#app = Display()

#if __name__ == '__main__':
#    print("Direct Call")
#    app.run()
#else:
#    print("From imported module")