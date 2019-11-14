def delete(records):
    ''' removes an entry from records
        1. Asks user for key (entry's owner's name)
        2. Check if entry exists
        3. Deletes the entry

        Input: dictionary
        Output: modifies dictionary
    '''
    owner = input("Please enter owner's name: ")
    if owner in records: # testing existence of owner key in records dictionary
        del records[owner]
    return records

def insert(records):
    ''' inserts a new entry

        Input: dictionary
        Output: the dictionary now has 1 new element
    '''
    owner = input("Please enter owner's name: ")
    balance = input("Please enter the balance: ")
    if not balance.isdigit(): # checking valid input for balance
        print(f"Invalid amount: ${balance}")
        return records
    balance = int(balance)
    memo = input("Please enter a memo: ")
    records[owner] = [balance, memo] # create key-value pair for the owner
    return records

def merge(records):
    ''' merges two entries into one
        the amounts are added together

        1. Asks user for two entries
        2. Creates new entry with sum amount
        3. Remove old two

        Input: dictionary
        Output: Modifies dictionary
    '''
    owner1 = input("Please enter first owner's name: ")
    if owner1 not in records:
        print(f"{owner1} not found")
        return records
    owner2 = input("Please enter second owner's name: ")
    if owner2 not in records:
        print(f"{owner2} not found")
        return records
    newOwner = input("Please enter new owner's name: ")
    if newOwner in records:
        print(f"{newOwner} already exists")
        return records
    memo = input("Please enter a memo: ")
    sum_amt = records[owner1][0] + records[owner2][0]
    records[newOwner] = [sum_amt, memo]
    del records[owner1]
    del records[owner2]
    return records

def print_all(records):
    ''' print all entries by a given topic

        Prints all entries like so:
        Name: Joe
        Amount: 20
        Memo: Tuesday

        Input: dictionary
        Output: prints all entries of records, dictionary unmodified
    '''
    for key, value in records.items():
        print(f"Name: {key}")
        print(f"Amount: {value[0]}")
        print(f"Memo: {value[1]}")
        print() # separator line

def print_menu():
    ''' prints available options
        Input: none
        Output: prints the list of options'''
    # a list of all available options
    print("Please pick 0-4:\n"
          "0. Exit\n"
          "1. Print all entries\n"
          "2. Add a new entry\n"
          "3. Delete an entry\n"
          "4. Merge entries")

def main():
    ''' Keeps track of a dictionary with key values as:
        {"Name" : [money(int), memos joined (string)]}
        User can choose to print entries, add or remove some, or merge them
    '''
    records = {}
    while True:
        print_menu()
        choice = input("Your choice: ")
        if choice == '0':
            break
        elif choice == '1':
            print_all(records)
        elif choice == '2':
            records = insert(records)
        elif choice == '3':
            records = delete(records)
        elif choice == '4':
            records = merge(records)
        else:
            print("Invalid option\n")

if __name__ == '__main__':
    main()