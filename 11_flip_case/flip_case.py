def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    """ 
    
    split string to list via list comprehension
    run or build relative match via case matches
    convert cases via if statements for case matches
    join via str


    """

    word_range = range(0, len(phrase))
    phrase_range = ''
    if to_swap.isupper():
        for x in word_range:
            if phrase[x].upper() == to_swap  and phrase[x].islower() == True:
                phrase_range += phrase[x].upper()
            else:
                phrase_range += phrase[x]
    print(phrase_range)
