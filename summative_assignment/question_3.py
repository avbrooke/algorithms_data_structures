def get_words_indices(text):
    indices = {}
    idx = 0

    while idx < len(text):
        if text[idx] == " ":
            idx +=1
            continue

        word_start = idx
        while idx < len(text) and text[idx] != " ":
            idx += 1
        word = text[word_start:idx].lower()

        if word in indices:
            indices[word].append(word_start)
        else:
            indices[word] = [word_start]

    return indices