import numpy as np


a = np.arange(12).reshape(-1,4)
print(a)

b = np.zeros_like(a)
c = np.zeros(a.shape, dtype="int32")
print(c)






# print(np.sum(a))
# print(np.sum(a, axis=0)) # 열의 합
# print(np.sum(a, axis=1)) # 행의 합



# a = np.zeros([3,4],dtype='int32')
# print(a)

# b = np.ones(10,dtype='int32')
# print(b)

