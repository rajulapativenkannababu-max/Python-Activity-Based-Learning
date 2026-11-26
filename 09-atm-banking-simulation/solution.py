# Case Study 38: ATM Menu-Driven Banking Simulation
# Syllabus used: variables, operators, conditional statements, loops, strings, lists

PIN = "2600"
MIN_BALANCE = 500          # minimum balance that must stay in the account
MAX_WITHDRAWAL = 20000     # per transaction limit
MAX_DEPOSIT = 50000        # per transaction limit

balance = 8500
history = []               # list of tuples (type, amount, balance after the operation)
attempts = 0
pin_ok = False

print("ATM MENU-DRIVEN BANKING SIMULATION")
print("Student : Rajulapati Venkanna Babu")
print("Roll No : 26000709")
print("-" * 50)

while attempts < 3 and pin_ok == False:
    entered = input("Enter your 4 digit PIN: ")
    attempts = attempts + 1
    if entered == PIN:
        pin_ok = True
    else:
        print("Incorrect PIN. Attempts left:", 3 - attempts)

if pin_ok == False:
    print("Card blocked - three wrong PIN attempts")
else:
    running = True
    while running:
        print()
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance enquiry")
        print("4. Transaction summary")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            amount = int(input("Enter the amount to deposit: "))
            if amount <= 0:
                print("REJECTED - deposit amount must be positive")
            elif amount > MAX_DEPOSIT:
                print("REJECTED - deposit limit is", MAX_DEPOSIT)
            else:
                balance = balance + amount
                history.append(("deposit", amount, balance))
                print("Deposit successful. New balance:", balance)

        elif choice == "2":
            amount = int(input("Enter the amount to withdraw: "))
            if amount <= 0:
                print("REJECTED - withdrawal amount must be positive")
            elif amount % 100 != 0:
                print("REJECTED - enter the amount in multiples of 100")
            elif amount > MAX_WITHDRAWAL:
                print("REJECTED - per transaction limit is", MAX_WITHDRAWAL)
            elif balance - amount < MIN_BALANCE:
                print("REJECTED - insufficient balance, minimum balance", MIN_BALANCE, "must be maintained")
            else:
                balance = balance - amount
                history.append(("withdrawal", amount, balance))
                print("Withdrawal successful. New balance:", balance)

        elif choice == "3":
            print("Available balance:", balance)

        elif choice == "4":
            if len(history) == 0:
                print("No transactions performed in this session")
            else:
                print()
                print("No  Type        Amount   Balance")
                print("-" * 40)
                count = 1
                for txn_type, amount, after in history:          # tuple unpacking
                    print(str(count).ljust(4), txn_type.ljust(12), str(amount).rjust(6), str(after).rjust(9))
                    count = count + 1
                print("-" * 40)
                print("Transactions :", len(history))
                print("Closing balance:", balance)

        elif choice == "5":
            print("Thank you for banking with us. Closing balance:", balance)
            running = False

        else:
            print("INVALID CHOICE - please enter a number from 1 to 5")
