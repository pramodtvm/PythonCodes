
class Difference:
    def __init__(self, a):
        self.__elements = a
        # print("values",self.__elements)

    def computeDifference(self):
        pass
        # self.__elements


    def maximumDifference(self):
        val = max(self.__elements) - min(self.__elements)
        return val
        # print ("val here",val)

    # Add your code here

# End of Difference class

#a = [int(e) for e in input().split(' ')]
a = [5,8,9,22,2]
d = Difference(a)
d.computeDifference()

print(d.maximumDifference)