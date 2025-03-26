user_input = input().strip()
first_part = ''
second_part = ''
delimiter_met = False
for symbol in user_input:
    if symbol == ',':
        delimiter_met = True
    elif not delimiter_met:
        first_part += symbol
    else:
        second_part += symbol
match_count = 0
for symbol in first_part:
    if symbol == second_part:
        match_count += 1
    else:
        break
print(match_count)
