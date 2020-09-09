from numpy import *
from pylab import *


# Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one.

n = int(input('Input a positive integer: '))

while n <= 0 or n > 10**6:
    n = int(input('Please input a POSITIVE integer that is LESS than a million'))


print(n)


list = [n]
while n != 1:


    if n % 2 == 0:
        n = int(n/2)
        list.append(n)
    else:
        n = int((n*3) + 1)
        list.append(n)

print('Here is the sequence of numbers the weird algorithm took to get to 1 from the chosen input:')
print(list)
