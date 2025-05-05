def get_words_indices(text):
    """
    Returns a dictionary that maps each given word to a list of starting indices where that word occurs.

    Words are case-insensitive.
    Words are assumed to be separated by at least one space, and have no punctuation.
    Args:
        text (str): The input string with words separated by space(s)
    Returns:
        dict: A dictionary in which each key is a lowercase word and the value is a list of starting
        indices where the word appears.
    """
    indices = {} # Dictionary for holding words and list of positions
    idx = 0 # Current index in the text

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