from numpy import *
from pylab import *
from random import *
# You are given all numbers between 1,2,…,n except one. Your task is to find the missing number.

n = int(input('input an integer '))
m = randrange(n)
l = list(range(n+1))
l.remove(m)
print(l)

#From here on, pretend we do not know m.

compareList = list(range(n+1))
print(compareList)

for x in range(n+1) :
    if l[x] != compareList[x]:
        print(compareList[x])
        break
