import math

test = int(input())

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for i in range(test):
    dem = 0
    n = int(input())
    for j in range(n):
        if math.gcd(n, j) == 1:
            dem += 1

    if isPrime(dem):
        print("YES")
    else:
        print("NO")
