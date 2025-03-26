website_url = input().strip()
segments = []
temp_segment = ""
for symbol in website_url:
    if symbol == '.':
        segments.append(temp_segment)
        temp_segment = ""
    else:
        temp_segment += symbol
segments.append(temp_segment)
for segment in reversed(segments):
    print(segment)