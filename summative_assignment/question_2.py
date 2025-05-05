import re

def molecule_to_list(molecule):
    """
    Converts a molecular formula string into a list of (atom, count) tuples.
    Args:
        molecule (str): A string representing a chemical formula.
    Returns:
        list: A list of tuples where each tuple contains an atom symbol (str) and its count (int).
    Raises:
        ValueError: If the molecule:
            - Doesn't start with an uppercase letter.
            - Contains non-alphanumeric characters.
            - Contains an invalid atom symbol (e.g. 'ca' instead of 'Ca').
            - Contains tokens not matching the original input.
            - Leaves characters unprocessed.
    """
    if not molecule or not molecule[0].isupper(): # Check molecule isn't empty string or doesn't start with lowercase
        raise ValueError("Molecule should start with an uppercase letter.")

    if not molecule.isalnum(): # Check if molecule only contains alphanumeric chars
        raise ValueError("Molecule should only contain alphanumeric characters.")

    # Regular expression pattern to extract atoms and counts
    pattern = r'([A-Z][a-z]?)(\d*)'
    tokens = re.findall(pattern, molecule)

    result = []
    idx = 0 # Track position in original molecule string

    for atom, count_string in tokens: # Check atom format is valid
        if not atom[0].isupper() or (len(atom)) == 2 and not atom[1].islower():
            raise ValueError("Atom format is not valid")

        valid = atom + count_string
        if molecule[idx:idx+len(valid)] != valid: # Check token matches molecule string at current index
            raise ValueError("Token does not align with original molecule")

        idx += len(valid)

        # Convert count to int, if empty default is 1
        count = int(count_string) if count_string else 1
        result.append((atom, count))

    # Check all characters in input were processed
    if idx != len(molecule):
        raise ValueError("Extra characters remain in the molecule string")

    return result