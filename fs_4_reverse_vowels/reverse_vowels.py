def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    temp_vowels = []
    temp_letters = []
    for letter in s:
        temp_letters.append(letter)
        if letter in vowels: 
            temp_vowels.append(letter)
    i = 0
    while i < len(temp_letters):
        if temp_letters[i] in vowels:
            temp_letters[i] = temp_vowels.pop()
        i += 1

    return ''.join(temp_letters)

