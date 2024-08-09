from interface import Interface

class InterfaceImp(Interface):
    
    def __init__(self, *args):
        self.args = args
        
    def method1(self):
        print(self.args)



