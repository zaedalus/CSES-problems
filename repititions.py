from numpy import *
from pylab import *


#You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.




#Input

#The only input line contains a string of n characters.

#Output

#Print one integer: the length of the longest repetition.


inputsequence = input()

print(inputsequence)
sequencelist = list(inputsequence)

alist = []
clist = []
tlist = []
glist = []

print(sequencelist)

for x in sequencelist:
    if x == 'A':
        alist.append('A')
    elif x == 'C':
        clist.append('C')
    elif x == 'G':
        glist.append('G')
    elif x == 'T':
        tlist.append('T')

print(max([len(alist),len(clist),len(tlist),len(glist)]))
