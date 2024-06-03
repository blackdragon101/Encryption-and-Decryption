password = 'rangers101'
def encryption():
    key = {'a': '2', 'b': '@', 'c': '-', 'd': '+', 'e': '|', 'f': '&', 'g': '3', 'h': '!', 'i': '#',
           'j': '%', 'k': '9', 'l': '^', 'm': '5', 'n': '$', 'o': '*', 'p': '6', 'q': '1', 'r': '?',
           's': '4', 't': '7', 'u': '~', 'v': '8', 'w': '<', 'x': '{', 'y': '0', 'z': '>'}
    random_words = 'abcdefghijklmnopqrstuvwxyz'
    sentence = input("Enter the sentence you want to encrypt: ")
    sen1 = sentence.lower()
    reverse = sen1[::-1]
    input_list = reverse.split()
    new_list = []
    for elements in input_list:
        list = []
        for letter in elements:
            list.append(key[letter])
        new_list.append(list)
    import random
    random_numbers = ''
    for words in new_list:
        for i in range(3):
            random_numbers += random.choice(random_words)
        words.append(random_numbers)
        random_numbers = ''
    print("The encrypted message is:")
    for elements in new_list:
        for code in elements:
            print(code,end='')
        print(end=' ')


    return
def decryption():
    code = {'a': '2', 'b': '@', 'c': '-', 'd': '+', 'e': '|', 'f': '&', 'g': '3', 'h': '!', 'i': '#',
           'j': '%', 'k': '9', 'l': '^', 'm': '5', 'n': '$', 'o': '*', 'p': '6', 'q': '1', 'r': '?',
           's': '4', 't': '7', 'u': '~', 'v': '8', 'w': '<', 'x': '{', 'y': '0', 'z': '>'}
    passing_word = input("Enter the password: ")
    if passing_word == password:
        print("You are granted permission for deciphering the message.")
        code_language = input("Enter the code you want to decipher: ")
        message1 = code_language.split()
        decipher_list = []
        for output in message1:
            message2 = ""
            for outs in output:
                if not outs.isalpha():
                    message2 += outs
            decipher_list.append(message2)
        decrypt_list = []
        for decipher in decipher_list:
            finale = ""
            for units in decipher:
                for keys,values in code.items():
                    if units == values:
                        finale += keys
                        reverse = finale[::-1]
                        break
            decrypt_list.append(reverse)
        final_list = []
        for i in range(len(decrypt_list)-1,-1,-1):
            final_list.append(decrypt_list[i])
        print("the decrypted form of your ciphered code is:")
        for elements in final_list:
            print(elements,end=" ")
choice = input("""Enter the number of the process you wish to proceed with:
                1.Encryption
                2.Decryption """)
if choice == '1':
    encryption()
elif choice == '2':
    decryption()





















































