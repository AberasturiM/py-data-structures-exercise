def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    # first try...
    # new_phrase = ''
    # for letter in phrase:
    #     if letter.lower() == to_swap.lower():
       
    #         if letter.islower():
    #             new_phrase += letter.upper()
    #         else:
    #             new_phrase += letter.lower()
    #     else:
    #         new_phrase += letter
    # return new_phrase
    
    # this is better...
    out = ''
    to_swap = to_swap.lower()
    
    for letter in phrase:
        if letter.lower() == to_swap:
            letter = letter.swapcase()
        out += letter
    
    return out