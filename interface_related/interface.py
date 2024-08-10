from abc import ABC, abstractmethod

class Interface(ABC):
    
    @abstractmethod
    def method1(self): ...


# class Interface2(ABC):
    
#     @abstractmethod
#     def method1(self, *args):
#         pass