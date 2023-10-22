def vigenere_encrypt(text, key):
    encrypted_text = []
    key = key.upper()
    text = text.upper()
    if any(char in key for char in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'):
        alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    elif any(char in key for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    key_length = len(key)
    for i in range(len(text)):
        if text[i] in alphabet and key_length > 0:
            key_char = key[i % key_length]
            key_idx = alphabet.index(key_char)
            text_idx = alphabet.index(text[i])
            new_idx = (text_idx + key_idx) % len(alphabet)
            encrypted_text.append(alphabet[new_idx])
        else:
            encrypted_text.append(text[i])

    return ''.join(encrypted_text)

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = []
    key = key.upper()
    encrypted_text = encrypted_text.upper()

    if any(char in key for char in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'):
        alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    elif any(char in key for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    key_length = len(key)
    for i in range(len(encrypted_text)):
        if encrypted_text[i] in alphabet and key_length > 0:
            key_char = key[i % key_length]
            key_idx = alphabet.index(key_char)
            text_idx = alphabet.index(encrypted_text[i])
            new_idx = (text_idx - key_idx) % len(alphabet)
            decrypted_text.append(alphabet[new_idx])
        else:
            decrypted_text.append(encrypted_text[i])

    return ''.join(decrypted_text)