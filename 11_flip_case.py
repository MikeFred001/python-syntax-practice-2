def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap_list = [to_swap.lower(), to_swap.upper()]

    for letter in phrase:
        if letter in to_swap_list:
            letter.swapcase()
        elif letter in to_swap_list:
            letter.swapcase()

    return phrase

# store uppercase and lowercase version of to-swap variable and evaluate those
# built-in swapcase method ==> letter.swapcase()

