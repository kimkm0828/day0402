import numpy as np

# 배열을 0으로                   zeros
# 배열을 1로                     ones
# 배열을 0,1이외의 다른값으로    full

# 연습 for문을 이용하여 행과 열을 바꿔서 출력
a = np.arange(12).reshape(-1,4)
print(a)
print(a[:,0])

# for i in range(4):
#     print(a[:,i])



# count = 0
# while count < 4:
#     for i in range(3):
#         print(a[i][count])
#         if i == 2:
#             count += 1






# a = np.ones([5,5],dtype=np.int32)
# print(a[0:5])
# a[1:4,1:4] = 0
# print(a)





# a = np.arange(12).reshape(-1,4)
# print(a)
# 행도 거꾸로 열도 거꾸로
# print(a[::][::-1])
# print(a[::-1,::-1]) # fancy indexing



# b = np.zeros_like(a)
# print(b)
#
# c = np.ones_like(a)
# print(a)
#
# d = np.full_like(a,100)
# print(d)





# print(np.cumsum(a))
# print(np.cumsum(a,axis=0))
# print(np.cumsum(a,axis=1))









# a = np.zeros([3,4],dtype=np.int32)
# b = np.ones([3,4],dtype=np.int32)
# c = np.full([3,4],100)
# print(a)
# print(b)
# print(c)


# a = np.zeros(10)
# b = np.ones(10)
# c = np.full(10,3)
#
# print(a)
# print(b)
# print(c)
