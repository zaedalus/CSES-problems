
#You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.




#Input

#The only input line contains a string of n characters.

#Output

#Print one integer: the length of the longest repetition.


inputSequence = str(input())

sepString = list(inputSequence)

i = 0
sCounter = 1
maxCounter = 1


while i+1 < len(sepString):
    if sepString[i] == sepString[i+1]:
        sCounter = sCounter + 1
    elif sepString[i] != sepString[i+1]:
        if sCounter >= maxCounter:
            maxCounter = sCounter
            sCounter = 1
        else: sCounter = 1
    i = i + 1

print(max([sCounter, maxCounter]))
