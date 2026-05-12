def reverse_string(text):
    if len(text) == 0:
        return text
    else:
        return reverse_string(text[1:]) + text[0]

print(reverse_string("Python"))
