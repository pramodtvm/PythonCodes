

class myclass():
    def __init__(self,x):
        self.x = x
        #self.y = y
        print("Initializing Variable")

    def add(self,a,b):
        print("Printing X",self.x)
        return a + b

    def subs(self,a,b):
        return a - b

c = input()
