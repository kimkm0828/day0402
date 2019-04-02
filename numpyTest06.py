import numpy as np

# 3개 다 똑같은 표현 -1은 알아서 해줘 라는 뜻
b = np.arange(6).reshape(2,3)
# b = np.arange(6).reshape(-1,3)
# b = np.arange(6).reshape(2,-1)
print(b)
print(b+1)
print(b>1)
# print(b[0])


# a = np.arange(3)
# print(a)
# print(a+1)  # broadCastiong
# print(a>1)  # broadCastiong
# print(a[a>1])  # broadCastiong