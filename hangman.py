import random

def getWord(fileName):
    with open(fileName, 'r') as file:
        word_list = file.read().split('\n') # assuming each word is on a separate line
    random.seed(3)
    i = random.randint(0, len(word_list)-1) # random index for word_list
    return word_list[i] # return a random word

def askAttempts():
    while True:
        num = input("How many incorrect attempts do you want? [1-25]\n")
        if not num.isdigit(): # checking if input is a positive integer
            print("Invalid input: Enter a number")
        elif not (1 <= int(num) <= 25): # if input is not in range 1-25
            print("Invalid input: Enter a number between 1 and 25 inclusive")
        else:
            break
    return int(num)

def askLetter(letters, num):
    while True:
        char = input("Choose the next letter:\n")
        if len(char) == 1:
            ascii = ord(char)
            if (65 <= ascii <= 90) or (97 <= ascii <= 122):  # if input is a valid letter
                char = char.lower() # converting letter guessed to lowercase
                if char not in letters:
                    break
                else:
                    print("Letter has been guessed already")
            else:
                print("Invalid input: Enter a letter")
        else:
            print("Invalid input: Enter a letter")
    return char

def display(word, letters):
    res = ""
    win = False
    for char in word:
        if char in letters:
            res += char
        else:
            res += '*'
    print(f"Word: {res}")
    if '*' not in res:
        win = True
    return win

def main():
    word = getWord("wordlist.txt")
    num = askAttempts()
    letters = []
    display(word, letters)
    for i in range(num, 0, -1):
        print(f"Attempts Remaining: {i}")
        print(f"Previous guesses: {letters}")
        char = askLetter()
        letters.append(char)
        win = display(word, letters)
        if win:
            break

    print(f"The word was {word}")
    if win:
        print("Congratulations! You won!")
    else:
        print("Try again next time!")
    user_in = input("Enter y/Y to try again")
    if user_in.toUpper() == 'Y':
        main()

if __name__ == '__main__':
    main()

