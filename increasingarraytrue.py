from random import *

inputSize = int(input())

inputArray = [int(i) for i in input().split()]
i = 0


counter = 0
i = 0


for j in inputArray:
    if i == inputSize - 1:
        break
    if inputArray[i+1] < j:
        difference = abs(inputArray[i+1] - j)
        inputArray[i+1] = inputArray[i+1] + difference
        counter += difference
    i += 1


print(counter)
