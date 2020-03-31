from typing import Dict


def reverse_dict_key_values(d: Dict):
    # make sure dict does not contain another dict
    a_value = list(d.values())[0]
    if isinstance(a_value, dict):
        raise ValueError(f'Cannot reverse an embedded dict')

    # assure all values are unique
    dict_values = []
    for dv in d.values():
        if dv not in dict_values:
            dict_values.append(dv)
        else:
            raise ValueError(f'Cannot reverse keys and values in dictionary because not all values are unique')

    inv_map = {v: k for k, v in d.items()}
    return inv_map
