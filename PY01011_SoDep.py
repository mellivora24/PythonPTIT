from itertools import product

digits = ['0', '2', '4', '6', '8']

def is_palindome(n):
    return n == n[::-1]

def gen_palindome(n):
    res = []

    length = 2
    while True:
        for num in product(digits, repeat=length):
            if num[0] == '0' or len(num) == 1:
                continue
            number = "".join(num)

            if is_palindome(number):
                if int(number) < n:
                    res.append(int(number))
                else:
                    return res
        length += 2

if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        n = int(input())
        res = gen_palindome(n)
        print(*res)
