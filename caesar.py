# Implements Caesar shift on some text

def caesar_shift(message, key, mode = 'ENCRYPT', custom_alphabet = None):
    final_message = ''
    if(custom_alphabet == None):
        for char in message:
            if char.isalpha():
                num = ord(char)
                num += key
                if char.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                elif char.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26
                final_message += chr(num)
            else:
                final_message += char
    else:
        testalphabet = 'xyzabc'
        for char in message:
            
    return final_message


    
