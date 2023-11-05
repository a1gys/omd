LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе
    >>> encode("SOS")
    '... --- ...'

    >>> encode("HOW ARE YOU@")
    Traceback (most recent call last):
        ...
    KeyError: '@'

    >>> encode("GOOD BYE EVERYONE SEE YoU TOMORROW")
    Traceback (most recent call last):
        ...
    KeyError: 'o'

    >>> encode("TOO LONG SENTENCE TO BE FIT IN ONE LINE SO WE USE ELLIPSIS") \
        # doctest: +ELLIPSIS
    '- --- ---   ...   . .-.. .-.. .. .--. ... .. ...'

    # Testing for NORMALIZE_WHITESPACE
    >>> encode("TESTING  WHITESPACES   WITH FLAGS")
    '- . ... - .. -. --.     .-- .... .. - . ... .--. .- -.-. . ...\
            .-- .. - ....   ..-. .-.. .- --. ...'
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)
