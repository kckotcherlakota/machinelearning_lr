import numpy as np 

f = np.array([2, 3, 1, 12,6])
f1=np.array([2,3,1,12,6])
f2=np.array([5,6,8,9,2])

a=0
k1=0
for i in f:
    a=a+i
k=len(f)
a=a/k#mean of 1st
for i in f2:
    k1=k1+i
n=len(f)
k1=k1/n#mean of second 
f=f-a
ff2=f.T
f2=f2-k1
qwf2=f2.T
#varience of f 

#varience of f2

qf2=f2.T
f2=f2.dot(qf2)/4
print(f2)
f=f.dot(ff2)/4
f=f.dot(qwf2)/4
print(f)
#finding the convarience of f,f2


#finding correlation

