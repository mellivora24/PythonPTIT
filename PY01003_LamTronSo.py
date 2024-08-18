test_case = int(input())

for i in range(test_case):
    n = input()
    process_n = [int(num) for num in n]
    index = len(process_n) - 1
    while index > 0:
        if process_n[index] >= 5:
            process_n[index - 1] += 1
        process_n[index] = 0
        index -= 1
    print("".join([str(num) for num in process_n]))

