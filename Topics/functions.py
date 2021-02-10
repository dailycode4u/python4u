def scan_letter(word:str,letters:str='aeiou') ->set:
    """returns a set of letters found in a phrase"""
    return set(letters).intersection(set(word))



