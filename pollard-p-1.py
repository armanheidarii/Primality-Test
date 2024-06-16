import math

n = 1943
B = 7

a = 2
for i in range(2, B + 1):
    a = (a**i) % n
    print(f"a in iteration {i} is {a}")

d = math.gcd(a - 1, n)
print(f"gcd {a-1} and {n} is {d}")

if 1 < d and d < n:
    print(f"Your factors are {d} and {n // d}")
else:
    print("We cannot decompose this number by Pollard p-1")
