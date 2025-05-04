import re

def molecule_to_list(molecule):
    if not molecule or not molecule[0].isupper():
        raise ValueError()

    if not molecule.isalnum():
        raise ValueError()

    pattern = r'([A-Z][a-z]?)(\d*)'
    tokens = re.findall(pattern, molecule)

    result = []
    idx = 0

    for atom, count_string in tokens:
        if not atom[0].isupper() or (len(atom)) == 2 and not atom[1].islower():
            raise ValueError()

        valid = atom + count_string
        if molecule[idx:idx+len(valid)] != valid:
            raise ValueError()

        idx += len(valid)

        count = int(count_string) if count_string else 1
        result.append((atom, count))

    if idx != len(molecule):
        raise ValueError()

    return result