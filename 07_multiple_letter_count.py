def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    frequency_counter = {}

    for char in phrase:
        frequency_counter[char] = frequency_counter.get(char, 0) + 1


    return frequency_counter
