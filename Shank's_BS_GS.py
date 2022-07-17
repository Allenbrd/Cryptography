# By Allen Bridi, 07/03/2022

import math

# Shank's babystep giantstep algorithm - Solving discrete log

print("DLP: g**x = h mod p")
g = int(input("Enter g: "))
h = int(input("Enter h: "))
p = int(input("Enter p: "))

n = 1 + math.floor(math.sqrt(p-1))  

H = g**(n*(p-2))%p

firstList = {}
for i in range(n):
    firstList[g**i %p] = i

for i in range(n):
    secondElement = (h*(H**i%p))%p
    if secondElement in firstList:
        print(i*n+firstList[secondElement])