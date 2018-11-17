# Implements Caesar shift on some text

def caesar_shift(message, key, mode = 'ENCRYPT', custom_alphabet = 'abcdefghijklmnopqrstuvwxyz'):
    final_message = ''
    default_alphabet = 'abcdefghijklmnopqrstuvwyz'
    for char in message:
        if char.isalpha():
            if(char.islower()):
                final_message += custom_alphabet[(default_alphabet.index(char) + key) % len(custom_alphabet)]
            elif(char.isupper()):
                final_message += custom_alphabet[(default_alphabet.index(char.lower()) + key) % len(custom_alphabet)].upper()
        else:
            final_message += char
    return final_message
    
print(caesar_shift("Usman", 1))