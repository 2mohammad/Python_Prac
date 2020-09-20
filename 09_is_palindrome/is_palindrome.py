def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    even_odd = len(phrase) % 2
    if even_odd == 1:
        mid_point = len(phrase) // 2
    elif even_odd == 0:
        mid_point = len(phrase) // 2 - 1
    word_range = range(0, len(phrase))
    phrase = phrase.replace(' ', '').upper()

    for x in word_range:
        if phrase[x] != phrase[len(phrase) - 1 - x] and x < mid_point:
            return False
        elif x == mid_point:
            return True
