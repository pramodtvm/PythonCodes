
""""




"""
from abc import ABC, abstractmethod

class AbstractClassExample(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass

class DoAdd42(AbstractClassExample):
    def do_something(self):
        return self.value + 42

class DoMul42(AbstractClassExample):
    def do_something(self):
        return self.value * 42


#x = DoAdd42(10)
#y = DoMul42(10)
#print(x.do_something())
#print(y.do_something())



"""
A class that is derived from an abstract class cannot be instantiated unless all of its abstract methods are overridden.

You may think that abstract methods can't be implemented in the abstract base class. This impression is wrong: 
An abstract method can have an implementation in the abstract class! Even if they are implemented, designers of 
subclasses will be forced to override the implementation. Like in other cases of "normal"
inheritance, the abstract method can be invoked with super() call mechanism. This makes it possible to provide some basic
functionality in the abstract method, which can be enriched by the subclass implementation.

"""

from abc import ABC, abstractmethod

class AbstractClassExample(ABC):
    def __init__(self):
        print("initializing Parent")
        me = 100
        self.varme = me

    @abstractmethod
    def do_something(self):
        print("Some implementation!",self.varme)

    def do_nothing(self):
        print("printing nothing",self.varme)

class AnotherSubclass(AbstractClassExample):
    def __init__(self):
        print("initialize child")

    def do_something(self):
        #super().__init__()
        #super().do_nothing()
        #super().do_something()
        print("The enrichment from AnotherSubclass")

#x = AnotherSubclass()
#x.do_something()
#x.do_nothing()
#d = AbstractClassExample()
