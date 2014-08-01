class Human:
    age = 0

    def __init__(self):
         self.name = 'John Doe'
    def setName(self, name):
         self.name = name
    def setAge(self, age):
         self.age = age
    def printHuman(self):
         print self.name
         print self.age
         print '\n'


BB = Human()
BB.printHuman()