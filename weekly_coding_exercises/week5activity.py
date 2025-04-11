
def encrypt_message(message, cipher_dict):
    message_encrypt = ""
    for char in message:
        if char in cipher_dict:
            message_encrypt += cipher_dict[char]
        else:
            message_encrypt += char
    return message_encrypt

def decrypt_message(message, cipher_dict):
    # Create a reverse cipher dictionary
    reverse_cipher_dict = {a: z for z, a in cipher_dict.items()}
    # Use the reverse cipher dictionary to decrypt the message
    return encrypt_message(message, reverse_cipher_dict)



simple_cipher= {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'y': 'b', 'z': 'a' }
print(encrypt_message("hello", simple_cipher))





