# By Allen Bridi, 07/03/2022

# Euler's Phi function

def phi(N):
    RPrimeToN = []
    for i in range(0, N):
        if math.gcd(i, N) == 1 :
            RPrimeToN.append(i)
    
    return len(RPrimeToN)