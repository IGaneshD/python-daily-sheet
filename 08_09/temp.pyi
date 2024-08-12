from abc import ABC, abstractmethod
class User(ABC):
    
    @abstractmethod
    def method1(self):...
    
    @abstractmethod
    def method2(self):...
    
    @abstractmethod
    @classmethod
    def get_object(cls):...