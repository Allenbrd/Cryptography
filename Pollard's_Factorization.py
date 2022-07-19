# By Allen Bridi, 07/09/2022
# Pollard's p-1 factorization algorithm

import math

N = int(input("Please enter an integer N to be factored: "))
a = 2
j = 1
while j:
    a = (a**j)%N
    d = math.gcd(a-1, N)
    if d > 1 and d < N:
        print(N,"=", d, "*", int(N/d))
        break
    else:
        j += 1