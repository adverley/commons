from typing import Dict


def reverse_dict_key_values(d: Dict):
    '''
    dict[key] = value --> dict[value] = key.
    This function does some basic sanity checks before inversing.
    :param d: Python Dict
    :return: same dict but with the values as keys and the keys as values
    '''

    # make sure dict does not contain another dict
    a_value = list(d.values())[0]
    if isinstance(a_value, dict):
        raise ValueError(f'Cannot reverse an embedded dict')

    # assure all values are unique
    if len(set(d.values())) != len(d.values()):
        raise ValueError(f'Cannot reverse keys and values in dictionary because not all values are unique')

    inv_map = {v: k for k, v in d.items()}
    return inv_map
