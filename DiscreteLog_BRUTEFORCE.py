# By Allen Bridi, 06/20/2022

# A brute force program to solve discrete logarithm

print("Congruence form: g^x ≡ h mod p")
g=int(input("Please enter a value for g: "))
h=int(input("Please enter a value for h: "))
p=int(input("Please enter a value for p: "))

for i in range(0, p):
    if g**i%p == h:
        print("Discrete logarithm: x=", i)
        break