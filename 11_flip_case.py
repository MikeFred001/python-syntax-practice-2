def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    case_flipped_phrase = ''

    for letter in phrase:
        if letter.lower() == to_swap.lower() and letter == letter.upper():
            case_flipped_phrase += letter.lower()
        elif letter.lower() == to_swap.lower() and letter == letter.lower():
            case_flipped_phrase += letter.upper()
        else:
            case_flipped_phrase += letter

    return case_flipped_phrase