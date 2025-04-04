# Q1 solution
def extract_text(text, keys):
    keys = keys.lower()
    words = text.split()
    valid = []
    for word in words:
        if all(k.lower() in keys for k in word):
            valid.append(word)
    return " ".join(valid)

data = "The term conda is not recognised as the name of a"
print(extract_text(data, "theAsORin"))

