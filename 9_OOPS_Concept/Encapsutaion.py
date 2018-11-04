

class Encapsulation(object):
    def __init__(self, a, b, c):
        self.public = a
        self._protected = b
        self.__private = c


c = Encapsulation(12,34,54)
print(c.public)
print(c._protected)
print(Encapsulation.__private)
print(c.__private)