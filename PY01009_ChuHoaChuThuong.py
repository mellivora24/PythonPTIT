text = input()

upper = 0
lower = 0

for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

if lower >= upper:
    print(text.lower())
else:
    print(text.upper())