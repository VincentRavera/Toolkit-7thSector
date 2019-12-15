import numpy as np


x = np.array([0, 1])
a = x*20
b = x*35
c = x*52
d = x*81
e = x*43
f = x*90
for i in a:
    for j in b:
        for k in c:
            for l in d:
                for m in e:
                    for n in f:
                            b = i+j+k+l+m+n
                            if b == 220:
                                print(i, j, k, l, m, n)
