a, K, N = map(int, input().split())
b = K - a%K # So b nho nhat de a + b chia het cho K

dem = 0
res = []
for i in range(a + b, N + 1, K):
    res.append(i-a)
    dem += 1

if dem != 0:
    print(*res)
else:
    print("-1")

