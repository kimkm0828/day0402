import numpy as np

a = ['160.7','180.5','145.8','175.5','162.5','154.3','169.1','156.5']
arr = np.array(a,dtype='float64')
print(arr[arr > 170])
