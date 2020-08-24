import winsound
import time

dot = 420
dash = dot * 3
space = 2.94
freq = 350


def morse(txt):
    encrypt = {'A':'.-', 'B':'-...', 'C':'-.-.',
               'D':'-..', 'E':'.', 'F':'..-.',
               'G':'--.', 'H':'....', 'I':'..',
               'J':'.---', 'K':'-.-', 'L':'.-..',
               'M':'--', 'N':'-.', 'O':'---',
               'P':'.--.', 'Q':'--.-', 'R':'.-.',
               'S':'...', 'T':'-', 'U':'..-',
               'V':'...-', 'W':'.--', 'X':'-..-',
               'Y':'-.--', 'Z':'--..', ' ':'|'}
    decrypt = {v: k for k, v in encrypt.items()}
    
    if '-' in txt:
        print("Audio transcription not available!")
        return ''.join(decrypt[i] for i in txt.split())
    return ' '.join(encrypt[i] for i in txt.upper())

code = input("Enter a message: ")

print(morse(code))

o = morse(code)

for char in o:
    if (char == '.'):
        winsound.Beep(freq, dot)
    elif (char == '|'):
        time.sleep(space)
    elif (char == ' '):
        time.sleep(1.2)
    else:
        winsound.Beep(freq, dash)
