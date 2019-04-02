import numpy as np

a = [1,2,3,4,5]
b = [1.0,2.0,3.0,4.0,5.0]
c = ['a','b','c','d','e','hello','우리나라 대한민국 가라가라 하와이에 가라가라 가락국수','이순신']
d = ['hello','java','python','oracle','mongo']
e = ['김경민','오상훈','이성기','김도희','정연미']


arr1 = np.array(a)
arr2 = np.array(b)
arr3 = np.array(c)
arr4 = np.array(d)
arr5 = np.array(e)
# dtype 요소 하나를 위한 자료형을 확인
# ndim  몇행인지(몇 차원인지) 확인인
#  shape 행과 열 확인
print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)
print(arr4.dtype)
print(arr5.dtype)