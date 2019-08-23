import numpy as np 

f = np.array([2, 3, 1, 12,6])
f2=np.array([5,6,8,9,2])
a=0
k1=0
for i in f:
    a=a+i
k=len(f)
a=a/k
for i in f2:
    k1=k1+i
n=len(f)
k1=k1/n
f=f-a
f2=f2-k1
f2=f2.T
f=f.dot(f2)/4
print(f)