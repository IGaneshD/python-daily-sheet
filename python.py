import timeit
import time

def countTobillion():
    start = time.time()
    i = 0
    while i<1_00_00_00_000:
        i+=1
    end = time.time()
    print(end-start)
    

countTobillion()

        
        
# print(timeit.timeit(stmt=countTobillion, globals=globals(), number=1))