import numpy as np

# 처음부터 넘파이 배열 생성하고싶다리
# arr = np.arange(1,7)
# print(arr)

# 파이썬배열 >> 넘파이배열로
a = [1,2,3,4,5,6]
arr1 = np.array(a)

# 넘파이배열  >> 파이썬 배열로
b = np.arange(6)
arr2 = list(b)


print(arr1)
print(arr2)