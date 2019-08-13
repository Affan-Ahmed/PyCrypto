# Main PyCrypto Class
def dechiper(message, type, key):
    if(type == 'CAESAR'):
        pass
        
def caesar_shift(message, shift, mode = 'ENCRYPT', custom_alphabet = 'abcdefghijklmnopqrstuvwxyz'):
    #key *= -1
    final_message = ''
    default_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in message:
        if char.isalpha():
            if(char.islower()):
                final_message += custom_alphabet[(default_alphabet.index(char) + shift) % len(custom_alphabet)]
            elif(char.isupper()):
                final_message += custom_alphabet[(default_alphabet.index(char.lower()) + shift) % len(custom_alphabet)].upper()
        else:
            final_message += char
    return final_message

print(caesar_shift("attack from south", 1, custom_alphabet="abc"))
print("hello")
print("hi")
