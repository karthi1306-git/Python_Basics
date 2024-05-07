import numpy as np

a = np.array([0,1.5,2,3,4,5])

print(a.size)
print(a.dtype)

#Indexing & Slicing Methods
ab = np.array([23,45,67,89,12])
ab[0]= 34
print(ab)
bc = ab[3:4]
print(ab[1:4])
print(bc)

#Vector Addition & Subraction
u = np.array([1,2,3])
v = np.array([4,5,6,])
z = u + v
y = u - v
x = u * v
aa = 2*u
print(z)
print(y)
print(x)
print(aa)


#Adding constant to Numpy
bb = np.array([9,8,7])
cc = bb +1
print(cc)
print(cc.max())


# 2D Array
a = [[11,12,13],[14,15,16],[17,18,19]]
A = np.array(a)
print(A)
print(A.ndim)
print(A.shape)
print(A.size)


A = "1234567"
print(A[1::2])

