def DauCuoi():
    text = input()

    dau = "".join([str(num) for num in text[0:2:1]])
    cuoi = "".join([str(num) for num in text[len(text)-2::1]])

    if int(dau) == int(cuoi):
        print("YES")
    else:
        print("NO")

test = int(input())
for i in range(test):
    DauCuoi()