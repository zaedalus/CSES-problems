# You are given all numbers between 1,2,…,n except one. Your task is to find the missing number.

n = int(input())
m = [int(i) for i in input().split()]

mLen = len(m)
mTotal = (mLen+1)*(mLen+2)/2
mSum = sum(m)

mValue = int(mTotal - mSum)

print(mValue)
