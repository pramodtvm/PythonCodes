import sys
sys.path.append(r"c:\dash\Tresuregram")
#import testing
#set PYTHONPATH="c:\dash\Tresuregram";%PYTHONPATH%
from Treasuregram.testing import caller
from Treasuregram.testing import myclassname
#sys.path.insert(0, 'c:\dash\Tresuregram')


def outer(num1):
    def inner_increment(num1):  # Hidden from outer code
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1, num2)
    print(locals())

#inner_increment(10)
#outer(10)

caller()
down = myclassname()
down.classfunc()
#print("my class name",down)


#print(mycar)
#testing.caller()