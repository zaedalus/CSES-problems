inputInteger = int(input())

inputSequence = list(range(1,inputInteger+1))
beautifulSequence = []


if inputInteger == 1:
    print(inputInteger)
elif inputInteger < 4:
    print('NO SOLUTION')
else:
    for i in range(2,inputInteger+1,2):
        beautifulSequence.append(i)
    for i  in range(1, inputInteger+1, 2):
        beautifulSequence.append(i)

print(*beautifulSequence)
