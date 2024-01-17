def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # first attempt...
    # letter_dict = {}
    # for letter in phrase:
    #     if letter in letter_dict:
    #         letter_dict[letter] += 1
    #     else:
    #         letter_dict[letter] = 1
    # return letter_dict      

    # this is better...
    counter = {}

    for ltr in phrase:
        counter[ltr] = counter.get(ltr, 0) + 1
    
    return counter