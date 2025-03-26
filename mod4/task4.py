text = input().strip()
char_count = {}
for symbol in text:
    char_count[symbol] = char_count.get(symbol, 0) + 1
odd_chars = [symbol for symbol, count in char_count.items() if count % 2]
if len(odd_chars) > 1:
    print("Невозможно составить палиндром")
else:
    left_half, middle_char = "", ""
    for symbol in sorted(char_count.keys()):
        occurrences = char_count[symbol]
        left_half += symbol * (occurrences // 2)
        if occurrences % 2:
            middle_char = symbol
    print(left_half + middle_char + left_half[::-1])