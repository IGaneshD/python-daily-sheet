from abc import ABC, abstractmethod

class Interface(ABC):
    
    @abstractmethod
    def method1(self, *args):
        print(*args)
    
    @abstractmethod
    def method2(self):
        raise NotImplementedError



