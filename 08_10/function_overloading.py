from functools import singledispatch

@singledispatch
def process(value):
    raise NotImplementedError("Cannot Process this type")


@process.register(int)
def _(value : int) -> None:
    print(" this is integer -->", value)

@process.register(str)
def _(value: str) -> None :
    print(" This is string -->", value)
    

process(15)
process("Hello")

