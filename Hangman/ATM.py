import random

# Generate random balance between £100 - £1000
balance = random.randint(100, 1000)

# Prompt user for PIN with 3 attempts
pin_attempts = 3
while pin_attempts > 0:
    pin = input("Please enter your 4 digit PIN: ")
    if pin.isdigit() and len(pin) == 4:
        break
    print("Invalid PIN format. Please enter 4 digits.")
    pin_attempts -= 1
else:
    print("Too many PIN attempts. Your card has been retained.")
    exit()

# Prompt user with options
options = {
    '1': 'Check balance',
    '2': 'Withdraw money',
    '3': 'Deposit money',
    '4': 'Exit'
}

while True:
    print("Please choose an option:")
    for key, value in options.items():
        print(f"{key}. {value}")
    transaction = input("Option: ")
    if transaction not in options:
        print("Invalid option. Please choose a valid option.")
        continue
    
    # Check balance
    if transaction == '1':
        print(f"Your current balance is £{balance}")
    
    # Withdraw money
    elif transaction == '2':
        while True:
            amount = input("Enter the amount you wish to withdraw: ")
            if not amount.isdigit():
                print("Invalid input. Please enter a valid amount.")
                continue
            amount = int(amount)
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            if amount > balance:
                print("Insufficient funds.")
                continue
            balance -= amount
            print(f"You have withdrawn £{amount}. Your current balance is £{balance}.")
            break
    
    # Deposit money
    elif transaction == '3':
        while True:
            amount = input("Enter the amount you wish to deposit: ")
            if not amount.isdigit():
                print("Invalid input. Please enter a valid amount.")
                continue
            amount = int(amount)
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            balance += amount
            print(f"You have deposited £{amount}. Your current balance is £{balance}.")
            break
    
    # Exit
    elif transaction == '4':
        print("Thank you for using this ATM. Goodbye!")
        break
    
    # Prompt user to continue or exit after each transaction
    continue_transaction = input("Do you wish to continue? (Y/N) ").upper()
    while continue_transaction not in ['Y', 'N']:
        continue_transaction = input("Invalid input. Do you wish to continue? (Y/N) ").upper()
    if continue_transaction == 'N':
        print("Thank you for using this ATM. Goodbye!")
        break
