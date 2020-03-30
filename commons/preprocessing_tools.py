def reverse_scale(values, max_value=None, range_values=None):
    '''

    brings
    [0.6, 0.7, 0.8, 0.9]
    to
    [0.9, 0.8, 0.7, 0.6]

    but not by reversing the list but by reverse scaling it

    :param values: list
    :param max_value: fill in if you have cached a value, otherwise calc it from values param
    :param range_values: fill in if you have cached a value, otherwise calc it from values param
    :return: reverse-scaled values
    '''
    max_ = max(values) if max_value is None else max_value
    range_ = max(values) - min(values) if range_values is None else range_values
    for s, grey_value in values.items():
        new_grey_value = max_ - (range_ - (max_ - grey_value))
        values[s] = new_grey_value

    return values
