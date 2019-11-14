def printMenu():
    ''' Receives algebraic operation desired on two numbers from user '''
    while True:
        op = input("Enter operation:\n"
                   "1. Addition\n"
                   "2. Subtraction\n"
                   "3. Multiplication\n"
                   "4. Division\n") # menu of algebraic operations
        if op == '': # enter = quit
            break
        if op == '1' or op == '2' or op == '3' or op =='4': # if user entered a valid operation
            num_in1 = num_in2 = ''
            while not num_in1.isdigit(): # keep asking for first number until valid number given
                num_in1 = input("Enter first number: ")
            while not num_in2.isdigit(): # keep asking for second number until valid number given
                num_in2 = input("Enter second number: ")
            num1 = int(num_in1) # convert string inputs into integers
            num2 = int(num_in2)
            if op == '1': # add
                res = addition(num1, num2)
                print(f"{num1} + {num2} = {res}\n")
            elif op == '2': # subtract
                res = sub(num1, num2)
                print(f"{num1} - {num2} = {res}\n")
            elif op == '3': # multiply
                res = mult(num1, num2)
                print(f"{num1} * {num2} = {res}\n")
            elif op == '4': # divide
                res = div(num1, num2)
                if res != None:
                    print(f"{num1} / {num2} = {res}\n")
        else:
            print("Invalid operation chosen\n")

def addition(num1, num2):
    ''' Adds the two numbers '''
    return num1 + num2

def sub(num1, num2):
    ''' Subtracts second number from first number '''
    return num1 - num2

def mult(num1, num2):
    ''' Multiplies the two numbers '''
    return num1 * num2

def div(num1, num2):
    ''' Divides the first number by the second number '''
    if num2 == 0:
        print("Cannot divide by zero\n")
        return
    return num1 / num2

def main():
    printMenu()

if __name__ == '__main__':
    main()
