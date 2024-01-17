def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    # first try...
    # vowel_dict = {}
    # vowels = ['a', 'e', 'i', 'o', 'u']
    # for letter in phrase:
    #     for vowel in vowels:
    #         if letter.lower() == vowel:
    #             if vowel in vowel_dict:
    #                 vowel_dict[vowel] += 1
    #             else:
    #                 vowel_dict[vowel] = 1
    # return vowel_dict

    # this is better...
    VOWELS = set("aeiou")
    
    phrase = phrase.lower()
    counter = {}

    for ltr in phrase:
        if ltr in VOWELS:
            counter[ltr] = counter.get(ltr, 0) + 1

    return counter