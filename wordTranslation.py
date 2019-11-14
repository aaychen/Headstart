def translate(alphabet, word):
    ''' Uses a dictionary called alphabet to translate word
        Does not modify original word
    '''
    new_word = ""
    for char in word: # iterating over each character in word
        new_word += alphabet[char] # alphabet[char] corresponds to the char in the new alphabet
    return new_word

def createAlphabet(charEncoding):
    ''' Turns a 26 char string called charEncoding into a dictionary,
        pairing each English letter to each character
    '''
    alphabet = {}
    ascii_num = 97 # starting with 'a'
    for char in charEncoding: # iterating over each character in the inputted encoding
        old_alph_char = chr(ascii_num) # convert ascii code
        alphabet[old_alph_char] = char # creating key-value pairs between letters of old alphabet and characters in new encoding
        ascii_num += 1 # increment ascii_num to get next letter of alphabet
    return alphabet

def main():
    ''' Translates a single word into another word using a new alphabet '''
    # get 26 char encoding for new alphabet from user
    while(True):
        encoding = input("Enter a 26 character encoding for the new alphabet\n"
                         "The first character replaces 'a', and the last character replaces 'z'\n")
        if(len(encoding) != 26):
            print("Encoding must be 26 characters long")
            continue
        else:
            break
    alphabet = createAlphabet(encoding)

    # translate words until user quits
    while(True):
        word = input("Enter a word to translate using the new encoding (Press enter to exit): ")
        if(word == ""):
            break
        new_word = translate(alphabet, word)
        print(f"Old Word: {word}")
        print(f"New Word: {new_word}")

if(__name__ == '__main__'):
    main()