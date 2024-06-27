class CharactersMapper:
    cyrillic_latin = {
        'љ': 'lj', 'њ': 'nj', 'е': 'e', 'р': 'r', 'т': 't', 'з': 'z', 'у': 'u', 'и': 'i', 'о': 'o', 'п': 'p',
        'ш': 'š', 'ђ': 'đ', 'ж': 'ž', 'а': 'a', 'с': 's', 'д': 'd', 'ф': 'f', 'г': 'g', 'х': 'h', 'ј': 'j',
        'к': 'k', 'л': 'l', 'ч': 'č', 'ћ': 'ć', 'ѕ': 's', 'џ': 'dž', 'ц': 'c', 'в': 'v', 'б': 'b', 'н': 'n',
        'м': 'm', 'Љ': 'Lj', 'Њ': 'Nj', 'Е': 'E', 'Р': 'R', 'Т': 'T', 'З': 'Z', 'У': 'U', 'И': 'I', 'О': 'O',
        'П': 'P', 'Ш': 'Š', 'Ђ': 'Ð', 'Ж': 'Ž', 'А': 'A', 'С': 'S', 'Д': 'D', 'Ф': 'F', 'Г': 'G', 'Х': 'H',
        'Ј': 'J', 'К': 'K', 'Л': 'L', 'Ч': 'Č', 'Ћ': 'Ć', 'Ѕ': 'S', 'Џ': 'Dž', 'Ц': 'C', 'В': 'V', 'Б': 'B',
        'Н': 'N', 'М': 'M'
    }

    @staticmethod
    def translate_to_latin(cyrillic_text: str) -> str:
        translated = ''.join(CharactersMapper.cyrillic_latin.get(c, c) for c in cyrillic_text)
        return translated

    @staticmethod
    def translate_responses(responses: list) -> list:
        translated_responses = []
        for sublist in responses:
            translated_sublist = [CharactersMapper.translate_to_latin(item) for item in sublist]
            translated_responses.append(translated_sublist)
        return translated_responses
    @staticmethod
    def header_convert(json_data):
        translated_data = [''.join(CharactersMapper.cyrillic_latin.get(c, c) for c in item) for item in json_data]
        return translated_data
