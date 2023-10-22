import time
import winsound

freq = 800
dotLength = 60
dashLength = dotLength * 3
pauseWords = dotLength * 7

morse_code = {
    'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---',
    'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-',
    'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-',
    'Э': '..-..', 'Ю': '..--', 'Я': '.-.-',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

reverse_morse_code = {value: key for key, value in morse_code.items()}


def text_to_morse(text):
    result = []
    for char in text.upper():
        if char in morse_code:
            result.append(morse_code[char])
    return ' '.join(result)


def morse_to_text(morse):
    result = []
    for char in morse.split(' '):
        if char in reverse_morse_code:
            result.append(reverse_morse_code[char])
    return ''.join(result)

def beep(dur):
    winsound.Beep(freq, dur)
def pause(dur):
    time.sleep(dur / 1000)

def morseaudio(morse):
    for char in morse:
        if char == ".":
            beep(dotLength)
        elif char == "-":
            beep(dashLength)
        elif char == "/":
            pause(pauseWords)
        else:
            pause(dashLength)