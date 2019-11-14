import random

def promptSeed():
    seedNum = int(input("Please enter a seed: "))
    return seedNum

def randomNums():
    random.seed(promptSeed())
    num1 = random.randint(1, 13)
    random.seed(promptSeed())
    num2 = random.randint(1, 13)
    random.seed(promptSeed())
    num3 = random.randint(1, 13)
    random.seed(promptSeed())
    num4 = random.randint(1, 13)
    return (num1, num2, num3, num4)

def printNums(nums):
    print("Here are your numbers:")
    for num in nums:
        print(num, end=' ')
    print("\n")

def promptExpression():
    print("Please enter an expression with a space after every number and operator")
    exp = input("Enter your expression:\n")
    return exp

def checkExpression(exp, nums):
    tokens = exp.split() # splitting expression into tokens by whitespace
    p_nums = []
    for item in tokens:
        if item != '**' and item != '//' and len(item) != 1: # checking spaces
            print("Invalid expression: Spaces are needed after every number and operator\n")
            return False
        if item.isdigit():
            if int(item) not in nums: # checking if numbers are valid
                print("Invalid expression: Only the 4 numbers displayed can be used\n")
                return False
            p_nums.append(int(item))

    # checking if each number was used once
    for num in p_nums:
        if p_nums.count(num) != nums.count(num):
            print("Invalid expression: You can only use each number once\n")
            return False
    return True

def computeExpression(exp):
    return eval(exp)

def printResults(val):
    if val == 24:
        print("\nCongratulations! Your expression is equal to 24!")
    else:
        diff = abs(val - 24)
        print(f"\nYou were {diff} off 24")

def setPlayAgain():
    ans = input("Do you want to play again? Enter 'yes' or 'no': ").strip()
    while (ans.lower() != 'yes') and (ans.lower() != 'no'):
        ans = input("Please enter 'yes' or 'no': ").strip()
    if ans.lower() == 'yes':
        print()
        main()
    else:
        print("Game ended")

def main():
    print("Starting a new game of 24")
    nums = randomNums()
    printNums(nums)
    valid = False
    while not valid:
        exp = promptExpression()
        valid = checkExpression(exp, nums)
    val = computeExpression(exp)
    printResults(val)
    setPlayAgain()

if __name__ == '__main__':
    main()
