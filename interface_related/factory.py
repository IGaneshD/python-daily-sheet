from interface import Interface

def objectfactory(cls, *args) -> Interface:
    obj = cls.__new__(cls)
    obj.__init__(*args)
    return obj