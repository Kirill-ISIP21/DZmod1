binary_string = input().strip()
zero_count = 0
one_count = 0

for digit in binary_string:
    if digit == '0':
        zero_count += 1
    elif digit == '1':
        one_count += 1

if zero_count == one_count:
    print("yes")
else:
    print("no")
