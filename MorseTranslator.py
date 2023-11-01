class MorseTranslator:
    # Dictionary mapping Morse code to characters
    morse_to_char = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
        '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7',
        '---..': '8', '----.': '9',
        '/': ' ', '|': ' '
    }

    @staticmethod
    def text_to_morse(text):
        """Convert text to Morse code"""
        morse_code = []
        for char in text.upper():
            if char == ' ':
                morse_code.append('|')
            elif char in MorseTranslator.morse_to_char.values():
                morse_code.append(next(key for key, value in MorseTranslator.morse_to_char.items() if value == char))
        return ' '.join(morse_code)

    @staticmethod
    def morse_to_text(morse_code):
        """Convert Morse code to text"""
        morse_words = morse_code.split(' ')
        text = ''
        for word in morse_words:
            if word in MorseTranslator.morse_to_char:
                text += MorseTranslator.morse_to_char[word]
            else:
                text += ' '
        return text
