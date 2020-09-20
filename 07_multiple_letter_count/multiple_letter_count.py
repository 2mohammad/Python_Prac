def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    word_range = range(0, len(phrase))
    lemons = dict((phrase[x], 0) for x in word_range)
    for keys, values in lemons.items():
        lemons[keys] =  len(phrase.split(keys)) - 1
    return lemons