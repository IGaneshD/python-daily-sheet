from abc import ABC, abstractmethod
import factory

class Interface(ABC):
    
    @abstractmethod
    def method1(self, *args): ...


# class Interface2(ABC):
    
#     @abstractmethod
#     def method1(self, *args):
#         pass

obj = factory.objectfactory(1,2,3,4)
obj.method1()