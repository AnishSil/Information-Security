import numpy as np
arr = np.array

h = arr([[1, 0, 1, 1, 1, 0, 0],
         [1, 1, 0, 1, 0, 1, 0],
         [0, 1, 1, 1, 0, 0, 1]])

k = 4
n = 7


p = h.transpose()
l = p
l = l[:4,:] 
eye = np.identity(k)
g = np.concatenate((eye,l), axis=1).astype('int32')

no = 2**k

u = []
for i in range(1,no+1):
    temp = []
    for j in range(k,0,-1):
        if ((i - 1) % (2**(-j + k + 1))) >= 2**(-j + k):
            temp.append(1)
        else:
            temp.append(0)
    u.append(temp)

c = np.mod(np.dot(u,g),2)
w_min = min(sum((c[1 : 2**k, :]).transpose()))

r = arr([0, 0, 0, 1, 0, 0, 0])
p = [g[:, n - k + 1 : n]]

ht = h.transpose()
s = np.mod(np.dot(r,ht),2)

for i in range(len(ht)):
    comp = ht[i] == s
    if comp.all():
        r[i] = 1-r[i]
        break

print(f"The error bit is {i}")
print(f"The corrected code is \n{r}")
