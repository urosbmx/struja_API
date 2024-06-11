import json
from transliterate import translit
def transliterate_dict(d):
    for key, value in d.items():
        if isinstance(value, dict):
            transliterate_dict(value)
        elif isinstance(value, str):
            d[key] = translit(value, 'sr', reversed=True)
        elif isinstance(value, list):
            for i in range(len(value)):
                if isinstance(value[i], dict):
                    transliterate_dict(value[i])
                elif isinstance(value[i], str):
                    value[i] = translit(value[i], 'sr', reversed=True)

