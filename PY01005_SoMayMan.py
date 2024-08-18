n = input()
num7 = 0
num4 = 0
for num in n:
    if num == '7':
        num7 += 1
    elif num == '4':
        num4 += 1

if num7 + num4 == 4 or num7 + num4 == 7:
    print("YES")
else:
    print("NO")
