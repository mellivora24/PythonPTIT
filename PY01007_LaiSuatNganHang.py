from cmath import log

test = int(input())

for i in range(test):
    n, x, m = map(float, input().split())
    x /= 100
    res = log(m/n, 1+x).real
    if res == int(res):
        print(int(res))
    else:
        print(int(res) + 1)
