def check(n):
    for char in str(n):
        if char not in ['4', '7']:
            return False
    return True


test = int(input())

for test_case in range(test):
    n = input()
    if check(n):
        print('YES')
    else:
        print('NO')
