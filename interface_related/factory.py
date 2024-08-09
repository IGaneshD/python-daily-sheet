from interface import Interface
from implementation import InterfaceImp

def objectfactory(*args) -> Interface:
    return InterfaceImp(*args)
