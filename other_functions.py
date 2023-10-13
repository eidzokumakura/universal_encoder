def atbash_encrypt(text):
    alphabet = "абвгдеёжзийкмнопрстуфхцчшщъыьэюя"
    encrypted_text = ""
    for char in text:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            encrypted_char = alphabet[-index-1]
            if char.isupper():
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def atbash_decrypt(text):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    decrypted_text = ""
    for char in text:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            decrypted_char = alphabet[-index-1]
        if char.isupper():
            decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text