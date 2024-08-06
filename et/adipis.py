# Unicode range for emoticons
emoticon_start = 0x1F600
emoticon_end = 0x1F64F

# Generate a list of emoticons within the specified range
emoticons = [chr(code_point) for code_point in range(emoticon_start, emoticon_end + 1)]

# Print all emoticons
for emoticon in emoticons:
    print(emoticon, end=" ")
