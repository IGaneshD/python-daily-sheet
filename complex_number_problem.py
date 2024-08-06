import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        self.number = complex(self.real, self.imaginary)
        
    def __add__(self, no):
        self.result = self.number + no.number
        self.imaginary = self.result.imag
        self.real = self.result.real
        return self.__str__()
        
    def __sub__(self, no):
        self.result = self.number - no.number
        self.imaginary = self.result.imag
        self.real = self.result.real
        return self.__str__()
        
    def __mul__(self, no):
        self.result = self.number * no.number
        self.imaginary = self.result.imag
        self.real = self.result.real
        return self.__str__()

    def __truediv__(self, no):
        self.result = self.number/no.number
        self.imaginary = self.result.imag
        self.real = self.result.real
        return self.__str__()

    def mod(self):
        self.result = math.sqrt(self.number.real**2 + self.number.imag**2)
        self.imaginary = self.result.imag
        self.real = self.result.real
        return self.__str__()

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')