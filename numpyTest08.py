import numpy as np

# 결론
# 차원이 다른것 끼리 연산이 가능한 형태
# 열의 수가 중요하며
# 두개의 배열의 열의수를 동일하게 하거나
# 열의수가 하나인것을 만들어 연산을 수행한후 원하는 차원으로 다시 만든다


a = np.arange(3)
b = np.arange(6)
c = np.arange(3).reshape(-1,3)
d = np.arange(6).reshape(-1,3)
e = np.arange(3).reshape(3,-1)


# print(a+b)
# print(a+c)
# print(a+d) # 이차원 배열과의 덧셈은 브로드캐스팅과 벡터 오퍼레이션 둘다 적용됨
# print(a+e)

print(a)
print(e)
# print(b)
# print(c)
# print(d)
# print(e)







# a = np.arange(3)
# b = np.arange(6)
#
# c = a + b
# print(c)
# ValueError: operands could not be broadcast together with shapes (3,) (6,)