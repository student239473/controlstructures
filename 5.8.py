balance = 1000  # Initial balance
pin = '1111'  # Initial 4-digit PIN code


def check_pin(entered_pin):
    """Verify the entered PIN matches the current PIN."""
    global pin
    return entered_pin == pin


def change_pin():
    """Allow the user to change their PIN."""
    global pin
    print("Change PIN:")
    old_pin = input("Enter your current PIN: ")
    if not check_pin(old_pin):
        print("Incorrect PIN. Returning to the menu.")
        return
    new_pin = input("Enter your new 4-digit PIN: ")
    if len(new_pin) == 4 and new_pin.isdigit():
        pin = new_pin
        print("PIN successfully changed!")
    else:
        print("Invalid PIN format. PIN must be exactly 4 digits.")


while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")
    print()

    if choice in {'1', '2', '3'}:
        entered_pin = input("Enter your PIN: ")
        if not check_pin(entered_pin):
            print("Incorrect PIN. Returning to the menu.")
            continue

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        change_pin()
    elif choice == '5':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")