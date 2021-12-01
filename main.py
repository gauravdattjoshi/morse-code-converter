# alphabets and numbers
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Morse Code of alphabets and numbers
alphabets_morse_code = [".-", '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
                        '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..- ', '...-', '.--', '-..-', '-.--', '--..']
numbers_morse_code = ['-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

# dictionaries of alphabets , numbers and final morse code

alphabets_morse_code_dict = dict(zip(alphabets, alphabets_morse_code))

numbers_morse_code_dict = dict(zip(numbers, numbers_morse_code))

morse_code_dict = alphabets_morse_code_dict | numbers_morse_code_dict


def morse_code_converter():

    enter_text = input('Enter the word to be converted to Morse code?\n').upper()
    morse_text = [f' {morse_code_dict[char]}' for char in enter_text]
    final_morse_code = (''.join(morse_text)).strip()
    print(f'The Morse Code is: {final_morse_code}')
    exit_func = input('Do you want to exit? Type "Y" to exit or any other character to continue.\n').lower()
    if exit_func == 'y':
        exit()
    else:
        return morse_code_converter()


morse_code_converter()


