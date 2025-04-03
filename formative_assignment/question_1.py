# Write a function extract_text(text, keys) that returns a string containing only words
# from the string text that are only composed of letters from the string keys. For simplicity we
# make the following assumptions:
# • The string text contains only alphabet letters and blank spaces, no numbers or
# punctuation,
# • the string keys is not empty,
# • the parameters provided will satisfy the two previous statements, and there is no need
# to check the inputs.
# In addition, the function must meet the following requirements:
# • each word in the returned string is separated by a single blank space,
# • the returned string does not start or end with a blank space,
# • the function should be case insensitive, that is the function should return the string
# ’Reader’ if the input text is ’Reader’ and the keys parameter is ’ArEdz’,
# • if the parameter text is an empty string, the function returns an empty string.

def extract_text(text, keys):
    text = text.lower()
    keys = keys.lower()
    for i in text:
        str_arr = list(i)
        for k in keys:
            if k in str_arr:
                print(i)

# TODO: returning correct chars that are present in keys, need to find a way to return it as strings of words present.

    # keys = keys.lower
    # has_upper = any(t.isupper() for t in text)
    # text_list = text.split()
    # print(text_list)
    # result = []

    # for text_list in text:
        # print(text_list)
        #
        # if any((t in text) for i in keys):
        #     result.append(t)
        #     return result


    # if any((i in text) for i in keys):
    #     result.append(text)
    #     return print(result)
    # else:
    #     return None


    # if text == "":
    #     return ""
    # else:
    #     if any((t in keys) for t in text):
    #         print('Found')
    #
    #     else:
    #         print('Not Found')



data = "The term conda is not recognised as the name of a"
print(extract_text(data, "theAsORin"))