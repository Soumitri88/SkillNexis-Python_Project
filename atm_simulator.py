# Simple ATM Simulator

balance = int(input("Enter your initial balance: "))
correct_pin = int(input("Enter your pin: "))

# Function to check balance
def check_balance():
    print("Your current balance is:", balance)

# Function to deposit money
def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        balance += amount
        print("Amount deposited successfully.")
        print("New balance:", balance)
    else:
        print("Invalid amount.")

# Function to withdraw money
def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print("Please collect your cash.")
        print("Remaining balance:", balance)


# PIN login
pin = int(input("Enter your PIN: "))

if pin == correct_pin:
    print("\nLogin successful!")

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance()

        elif choice == 2:
            deposit()

        elif choice == 3:
            withdraw()

        elif choice == 4:
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice.")

else:
    print("Incorrect PIN. Access denied.")