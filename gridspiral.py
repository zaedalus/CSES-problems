testNumber = int(input())
n = 0
testArray = []

while n < testNumber:
    testLines = input().split()
    testArray.append(testLines)
    n += 1

for j in testArray:
    if int(j[1]) >= int(j[0]):
        if int(j[1])% 2 == 1:
            outputValue = int(j[1])**2 - int(j[0]) + 1
            print(outputValue)
        else:
            outputValue = (int(j[1])-1)**2 + int(j[0])
            print(outputValue)
    else:
        if int(j[0])%2 == 0:
            outputValue = int(j[0])**2 - int(j[1]) + 1
            print(outputValue)
        else:
            outputValue = (int(j[0])-1)**2 + int(j[1])
            print(outputValue)
