def convert_to_binary(value):
    if value == 0:
        return "0"
    bin_result = ""
    while value > 0:
        bin_result = str(value % 2) + bin_result
        value = value // 2
    return bin_result

def convert_to_octal(value):
    if value == 0:
        return "0"
    oct_result = ""
    while value > 0:
        oct_result = str(value % 8) + oct_result
        value = value // 8
    return oct_result

def convert_to_hex(value):
    if value == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hex_result = ""
    while value > 0:
        hex_result = hex_chars[value % 16] + hex_result
        value = value // 16
    return hex_result

user_input = input().strip()
if not user_input.isdigit() or int(user_input) <= 0:
    print("Ошибка: введите положительное число")
else:
    number = int(user_input)
    binary_output = convert_to_binary(number)
    octal_output = convert_to_octal(number)
    hex_output = convert_to_hex(number)
    print(f"{binary_output}, {octal_output}, {hex_output}")