from math import sqrt

def checkifPrime(number):
    root = int(sqrt(number)) + 1
    
    for i in range(2, root):
        if number%i==0:
            break
    else:
        return number
    
    return None
            

def printPrimeNumbers(n):
    count = 0
    current_number = 2
    while count<n:
        
        if checkifPrime(current_number):
            print(current_number)
            count += 1
        
        current_number += 1


printPrimeNumbers(10)
