def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    word_range = range(1, len(phrase)+1)
    return "".join([phrase[-x] for x in word_range])
