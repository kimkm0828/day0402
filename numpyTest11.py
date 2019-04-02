import numpy as np

#점수가 가장 높은 학생
name = np.array(['차범근','홍길','강감','이순','유관','김경','파추호'])
score = [100,80,90,100,70,95,100]
# r = np.argmax(score)
r = np.argwhere(score == np.amax(score))
print(name[r])



# a = [4,3,1,5,2,2,5,5]
# arr1 = np.array(a)
# r = np.max(arr1)
# idx = np.argmax(arr1)
# print(r)
# print(idx)



# name = ['홍길','강감','이순','유관','박주호','김경','문재인']
# score = [80,90,100,70,100,95,100]
# a = np.argsort(score)[::-1]
# b = np.array(name)
# print(b[a])








# a = [4,3,1,5,2]
# arr1 = np.array(a)
# b = np.argsort(arr1)
# print(b)


# a = [4,3,1,5,2]
# arr1 = np.array(a)
# arr1.sort()
# print(arr1)


# a = [1,3,0,3,1]
# b = np.eye(len(a),np.max(a)+1,dtype='int32',)[a]
# print(b)





# 대각선 만들어줌
# a = np.eye(5,5)
# print(a)




# a = [1,3,0,3,1]
# a배열의 요소만큼 행의 크기를 갖고 a배열의 요소중 최댓값+1의 열의 크기를 같는
# 0으로 채워진 2차원 배열을 만들고
# 각행마다 a배열의 요소 만큼 열에 1을 채움

#------------------내가 햇던짓
# max = a[0]
# for i in range(len(a)):
#     if max < a[i]:
#         max = a[i]
# arr = np.zeros([len(a),max+1],dtype='int32')
# for i in range(len(a)):
#     arr[i,a[i]] = 1
# print(arr)

# 모범 답안
# arr = np.zeros([len(a),np.max(a)+1],dtype='int32')
# arr[[range(len(a))],a] = 1
# print(arr)





# arr = np.zeros([5,5],dtype='int32')
# for i in range(5):
#     arr[i,i] = 1
#
# print(arr)

# for i in range(5):
#     arr[i,4-i] = 1
#
# print(arr)










# 연습
# 테두리가 1로 채워지고 속은 0으로 채워진 5*5
# arr = np.zeros([5,5],dtype='int32')
# print(arr)
# arr[:,[0,-1]] = 1
# arr[[0,-1],:] = 1
# print(arr)

# a = np.ones([5,5],dtype='int32')
# print(a)
# a[1:-1,1:-1] = 0
# print(a)




#----------------------------------------
# a = np.arange(12).reshape(-1,4)
# print(a)
# #       행  행  열 열
# print(a[[1, 0],[0, 1]])
#
# a[[1,0],[0,1]] = 100
# print(a)



# print(a)
# print(a>5)
# print(a[a>5]) # bool array

# print(a[0,1])
# print(a[0,1])
# print(a[[0,1]])
# print(a[[1,0]])