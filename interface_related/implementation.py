from interface import Interface
from factory import objectfactory

class InterfaceImp(Interface, object):
    
    def __init__(self, *args):
        self.args = args
        
    def method1(self):
        print(self.args)


obj = objectfactory(InterfaceImp, 1,2,3,4)
obj.method1()