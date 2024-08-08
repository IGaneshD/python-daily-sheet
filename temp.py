# data = [1,2,3,4,5,6,7,8,9,10]
# dict_ = {"odd":[],"even":[]}

# dict_["odd"].extend(filter(lambda x:x%2, data))
# dict_["even"].extend(filter(lambda x: x%2==0, data))


# import timeit

# def whileFunction():
#     i = 0
#     while i<1_00_00_000:
#         i+=1

# def forFunction():
#     for i in range(1_00_00_000):
#         pass   

# print(timeit.timeit("whileFunction()", globals=globals(), number=5))
# print(timeit.timeit("forFunction()", globals=globals(), number=5))

from abc import ABC, abstractmethod


