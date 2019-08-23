import numpy as np 

f = np.array([2, 3, 1, 12,6])
f2=np.array([5,6,8,9,2])
a=0
k1=0
for i in f:
    a=a+i
k=len(f)
a=a/k

f=f-a
f2=f.T
f=f.dot(f2)/4
print(f)