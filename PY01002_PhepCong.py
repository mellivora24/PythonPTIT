input_text = input()
process_input = input_text.split()
a = int(process_input[0])
b = int(process_input[2])
c = int(process_input[4])

if a + b == c:
    print("YES")
else:
    print("NO")

