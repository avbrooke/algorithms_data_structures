
def ispalindrome(word):
    """Function checking if the text without spaces and punctuation is a palindrome.

    Args:
        word (str): the text to check if it is a palindrome

    Returns:
        bool: True if the text is a palindrome, False otherwise
    """

    # Base case (1): if the size of the word is 1 or less it is a palindrome
    if len(word) <= 1:
        return True
    # Recursive case: if the first character is not a letter, skip it
    if not word[0].isalpha():
        return ispalindrome(word[1:])
    # Recursive case: if the last character is not a letter, skip it
    if not word[-1].isalpha():
        return ispalindrome(word[:-1])
    # Base case (2): if the first and last characters are different, it is not a palindrome
    if word[0].upper() != word[-1].upper():
        return False
    # Recursive case: if the first and last characters are the same, check the rest of the word
    # by removing the first and last characters
    return ispalindrome(word[1:-1])


def rec_sum(numbers):
    # Base case: if the list is empty, the sum is 0
    if numbers == []:
        return 0
    # Recursive case: add the first number to the sum of the remaining
    # numbers in the list
    return numbers[0] + rec_sum(numbers[1:])


def sum_digits(number):
    # Recursive case: if the number is negative, call the function with
    # the positive number
    if number < 0:
        return sum_digits(-number)
    # Base case: if the number is 0, the sum of its digit is 0
    if number == 0:
        return number
    # pedagogic comment: The following two statements separate the last
    # digit from the rest of the number using modular arithmetic:
    # [number = 10 x quotient + remainder]
    quotient = number // 10
    digit = number % 10
    # Recursive case: add the last digit to the sum of the preceding digits
    return digit + sum_digits(quotient)


def flatten(mlist):
    # Base case: if the list is empty, the result is an empty list
    if mlist == []:
        return []
    # If the list is not empty, we have two cases depending on the type of
    # the first element:
    # 1- Recursive case: if the first element is a list, flatten it and
    #    concatenates the flattened rest of the list to it
    # 2- Base case: if the element is a number (i.e not a list), return a list
    #    containing the number. We need to return a list because the result of
    #    the function is a list.
    if isinstance(mlist, list):
        return flatten(mlist[0]) + flatten(mlist[1:])
    return [mlist]


def merge(sorted_listA, sorted_listB):
    # Base case: if one of the lists is empty, return a copy of the other list
    if sorted_listA == []:
        return sorted_listB[:]
    # Base case: if one of the lists is empty, return a copy of the other list
    if sorted_listB == []:
        return sorted_listA[:]
    # Recursive case: if the first element of the first list is smaller than
    # the first element of the second list, add the first element of the first
    # list to the merged list and merge the rest of the first list and the
    # second list. Append the resulting list to the first element of the first
    # list.
    if sorted_listA[0] < sorted_listB[0]:
        return [sorted_listA[0]] + merge(sorted_listA[1:], sorted_listB)
    # Recursive case: if the first element of the second list is smaller than
    # the first element of the first list, add the first element of the second
    # list to the merged list and merge the rest of the second list and the
    # first list. Append the resulting list to the first element of the second
    # list.
    return [sorted_listB[0]] + merge(sorted_listA, sorted_listB[1:])

def iselfish(word):
    def _iselfish_helper(word, pattern):
        # Base case: if the pattern is empty, the word is elfish
        if pattern == []:
            return True
        # Base case: if the word is empty, the word is not elfish
        # because it does not contain all the letters in the pattern
        # otherwise the pattern would be empty.
        if word == '':
            return False
        # Recursive case: there are two cases to consider:
        # 1)- if the first letter of the word is in the pattern,
        #     remove it from the pattern and continue checking the rest of
        #     the word
        # 2)- if the first letter of the word is not in the pattern,
        #     continue checking the rest of the word without removing the
        #     letter from the pattern.
        if word[0] in pattern:
            pattern.remove(word[0])
            return _iselfish_helper(word[1:], pattern)
        return _iselfish_helper(word[1:], pattern)

    return _iselfish_helper(word,['e', 'l', 'f'])