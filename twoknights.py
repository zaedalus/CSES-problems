boardSize = int(input())**2

i = 1

if boardSize == 1:
    print(int(0))
else:
    while i**2 <= boardSize:
            kPermut = ((i**2)*(i**2 - 1))/2 - (4*(i - 1)*(i - 2))
            print(int(kPermut))
            i += 1
