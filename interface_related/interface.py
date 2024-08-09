from abc import ABC, abstractmethod
import factory as f

class Interface(ABC):
    
    @abstractmethod
    def method1(self, *args): ...


# class Interface2(ABC):
    
#     @abstractmethod
#     def method1(self, *args):
#         pass





if __name__=="__main__":
    obj = f.objectfactory(1,2,3,4)
    obj.method1()