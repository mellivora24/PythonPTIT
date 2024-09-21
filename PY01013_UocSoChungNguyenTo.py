import math

def list_gcd(a, b):
    res= []
    gcd = math.gcd(a, b)
    while gcd > 0:
        res.append(gcd%10)
        gcd = gcd // 10
    return res

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

test = int(input())
for _ in range(test):
    a, b = map(int, input().split())
    res = list_gcd(a, b)

    sum = 0
    for i in res:
        sum += i

    if is_prime(sum):
        print("YES")
    else:
        print("NO")
