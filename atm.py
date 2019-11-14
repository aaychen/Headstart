def login(pin):
    ''' Checks if user enters correct pin within 3 tries'''
    correct = False
    for i in range(3): # user gets 3 tries to enter pin correctly
        user_in = input("Enter 4-digit pin: ")
        if(user_in == pin):
            correct = True
            print("Logged in successfully!")
            break
        else:
            print("Login failed")
    if(not correct):
        print("Too many failed attempts")
    return correct

def printMenu(balance):
    ''' Asks user what they would like to do '''
    hist = ["Account Creation"]
    while(True):
        print(f"Current balance: {balance}")
        choice = input("Please pick 1-4\n"
                        "1. Deposit\n"
                        "2. Withdraw\n"
                        "3. View past transactions\n"
                        "4. Log out\n")
        if(not choice.isdigit()):
            continue
        if(choice == '1'):
            amt = input("Enter amount to deposit: ")
            balance = deposit(balance, amt)
            hist.append("Deposited $" + amt) # record deposit transaction into hist list
        elif(choice == '2'):
            amt = input("Enter amount to withdraw: ")
            balance, withdrawn = withdraw(balance, amt)
            if(withdrawn):
                hist.append("Withdrew $" + amt) # record withdrawal transaction into hist list
        elif(choice == '3'):
            printHistory(hist)
        elif(choice == '4'):
            print("Thank you for using the ATM!")
            break
    return hist

def deposit(balance, amt):
    ''' Checks for valid input and deposits money into account '''
    if(not amt.isdigit()): # checking for invalid input
        print("Invalid amount\n")
    else:
        amt = int(amt) # convert amt to an integer
        balance += amt
        print(f"Deposited {amt}\n")
    return balance

def withdraw(balance, amt):
    ''' Checks for valid input and withdraws money if balance holds sufficient funds '''
    withdrawn = False # if withdrawn money or not
    if(not amt.isdigit()): # checking for invalid input
        print("Invalid amount\n")
    else:
        amt = int(amt) # convert amt to an integer
        if(amt <= balance):
            balance -= amt
            print(f"Withdrew {amt}\n")
            withdrawn = True
        else:
            print("Not enough in balance\n")
    return balance, withdrawn

def printHistory(hist):
    ''' Outputs every previous transaction '''
    for item in hist: # iterates over each item in hist list
        print(item)
    print() # line separator

def logout(file, pin, hist):
    ''' Writes history of transactions to a file '''
    with open(file, 'w') as outfile:
        outfile.write(str(pin) + "\n") # writes pin number to outfile
        for item in hist:
            outfile.write(str(item)+"\n") # writes item to outfile

def main():
    ''' Simulates an ATM machine with login, deposit, and withdrawal functions '''
    fileName = input("Enter a file to read: ")
    with open(fileName, 'r') as infile: # reading in file
        fileData = infile.read().split('\n') # fileData elements are lines of infile
    pin = fileData[0] # first element of fileData (first line of infile) is the pin number

    correct = login(pin)
    if(correct): # if user entered correct pin
        hist = printMenu(0)
        logout(fileName, pin, hist)

if(__name__ == '__main__'):
    main()