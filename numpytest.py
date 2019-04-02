import numpy as np

a = [0,1,2,3,4,5]
arr = np.array(a)

arr2 = arr.reshape(2,3)
print(arr.shape)
print(arr2.shape)   # 몇행 몇열인지?

print(arr.ndim)  # 몇차원인지?


# b = np.array(5)
#
# c = np.array(a)
#
# print(c)
# print(type(c))