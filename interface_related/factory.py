from interface import Interface

def objectfactory(*args, cls) -> Interface:
    # super(type, object)
    # obj = super(cls, cls).__new__(cls)
    obj = cls.__new__(cls)
    obj.__init__(*args)
    return obj