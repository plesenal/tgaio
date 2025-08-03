def caesar_cipher_decrypt(text, shift, alphabet):
    decrypted_text = ""
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            decrypted_char = alphabet[(char_index - shift) % len(alphabet)]
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # Если символ не в алфавите, оставляем его без изменений
    return decrypted_text

def all_possible_decryptions(cipher_text, alphabet):
    for key in range(len(alphabet)):
        decrypted_text = caesar_cipher_decrypt(cipher_text, key, alphabet)
        print(f'Key {key}: {decrypted_text}')

# Определим наш алфавит и зашифрованное слово
alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'  # Алфавит русского языка
cipher_text = 'КАЛАКАЖЫ'

# Выводим все возможные расшифровки
all_possible_decryptions(cipher_text, alphabet)
