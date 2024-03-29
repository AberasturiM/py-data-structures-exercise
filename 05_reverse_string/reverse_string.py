def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    # first attempt...
    # phrase_list = list(phrase)
    # phrase_list.reverse()
    # return ''.join(phrase_list)

    # this is better...
    return phrase[::-1]