def backwards(text):
    if len(text) <= 1:
        return text

    return backwards(text[1:]) + text[0]
string = "ojsan"
run = backwards(string)
print(run)