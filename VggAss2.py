jsonData = {
    "test@gmail.com": {"pwd": "12345", "balance": 500.00}
}
 

 
def create_account():
    print("Thank you for your interest in Banking with us,\nPlease enter your details correctly")
    print("=========================================\n=========================================")
    email = input("Enter your email  ").lower()
    if ("@" in email) and ("." in email):
        if email in jsonData.keys():
            print("Account with this email already exists")
        else:
            password = input("Enter your password  ")
            balance = 0.0
            jsonData[email] = {"password": password, "balance": balance}
            print(jsonData)
            print("Account created successfully, Proceed to make a transaction")
    else:
        print("Email is not valid, Please try again")
        create_account()
 
 
def transaction():

    print("Dear Customer, Welcome!")
    print("                                         \n                                         ")
    email = input("Please enter your email  ").lower()
    # check if user exists or not
    if email not in jsonData.keys():
        print("Sorry Account does not exist, Please Create account")
    else:
        password = input("Please enter your password  ")
       
        if password == jsonData[email]["password"]:
            print("Dear Customer, you have been authenticated")
            print("Please proceed to select a transaction type")
            print("=========================================\n=========================================")
            print("                                         \n                                         ")
           
            transactionAction = input("Press 1: Check balance\nPress 2: Deposit\nPress 3: Withdraw\nPress4: send")
            print("                                         \n                                         ")
            if transactionAction == "1":
                check_balance(email)
 
            elif transactionAction == "2":
                deposit(email)
 
            elif transactionAction == "3":
                withdraw(email)
 
            elif transactionAction == "4":
                send(email)
 
            else:
                print("Invalid selection")
 
        else:
            print("Incorrect Password")
            create_account()
 
 
def check_balance(email):
    
    balance = jsonData[email]["balance"]
    print("Your balance is ", balance)
    print("===============================")
    print("Thank you for jsonDataing with us")
    quit()
 
 
def deposit(email):
    """Deposit funds"""
    amount = input("Please Enter an amount you want to deposit")
    while True:
        try:
            valid_amount = float(amount)
            if valid_amount > 0.0:
                break
            else:
                print("Invalid amount, please enter figures only")
                amount = input("Please Enter an amount you want to deposit")
        except ValueError:
            print("Invalid amount, please enter figures only")
            amount = input("Please Enter an amount you want to deposit")
    current_balance = jsonData[email]["balance"]
    jsonData[email]["balance"] = current_balance + valid_amount
    new_balance = jsonData[email]["balance"]
    print("You have deposited ", valid_amount, "Your new balance is ", new_balance)
    print("===============================")
    print("Thank you for jsonDataing with us")
 
 
def withdraw(email):
    """Withdraw funds"""
    withdrawal_amount = input("Please enter an amount to withdraw")
    # check if there is sufficient balance for the transaction
    while True:
        try:
            valid_withdrawal_amount = float(withdrawal_amount)
            if valid_withdrawal_amount > 0.0:
                break
            else:
                print("Invalid amount, please enter figures only")
                withdrawal_amount = input("Please enter an amount to withdraw")
        except ValueError:
            print("Invalid amount, please enter figures only")
            withdrawal_amount = input("Please enter an amount to withdraw")
    current_balance = jsonData[email]["balance"]
    if current_balance < valid_withdrawal_amount:
        print("Insufficient funds, your current balance is", current_balance)
        print("Would you make a DEPOSIT now? Yes or No")
        option = input()
        if option.lower() == "yes":
            deposit(email)
        elif option.lower() == "no":
            print("===============================")
            print("Thank you for jsonDataing with us")
            quit()
        else:
            print("Invalid selection")
    else:
        jsonData[email]["balance"] = current_balance - valid_withdrawal_amount
        new_balance = jsonData[email]["balance"]
        print("You have withdrawn", withdrawal_amount, "Your new balance is ", new_balance)
        print("===============================")
        print("Thank you for jsonDataing with us")
 
 
def send(email):
    """send funds"""
    recipient = input("Please enter the beneficiary's email id").lower()
    if recipient not in jsonData.keys():
        print("Beneficiary account does not exist, Please try again")
        send(email)
    send_amount = input("Please enter the amount to send")
    while True:
        try:
            valid_amount = float(send_amount)
            if valid_amount > 0.0:
                break
            else:
                print("Invalid amount, please enter figures only")
                send_amount = input("Please enter the amount to send")
        except ValueError:
            print("Invalid amount, please enter figures only")
            send_amount = input("Please enter the amount to send")
    current_balance = jsonData[email]["balance"]
    # check if there is sufficient balance for the transaction
    if current_balance < valid_amount:
        print("Insufficient funds, your current balance is", current_balance)
        print("Would you make a DEPOSIT now? Yes or No")
        option = input()
        if option.lower() == "yes":
            deposit(email)
        elif option.lower() == "no":
            print("===============================")
            print("Thank you for jsonDataing with us")
            quit()
        else:
            print("Invalid selection")
    else:
        jsonData[email]["balance"] = current_balance - valid_amount
        new_balance = jsonData[email]["balance"]
        recipient_balance = jsonData[recipient]["balance"]
        jsonData[recipient]["balance"] = recipient_balance + valid_amount
        print("You have sendred", valid_amount, "to", recipient, "Your new balance is ", new_balance)
        print("===============================")
        print("Thank you for jsonDataing with us")
 
 
prompt = input("Press 1: Create Account \nPress 2: Transaction \nPress E to exit ")
while True:
    if prompt == "1" or prompt == "2" or prompt == "E":
        break
    else:
        print("Invalid selection")
        prompt = input("Press 1: Create Account \nPress 2: Transaction \nPress q to quit ")
if prompt == "1":
    create_account()
elif prompt == "2":
    transaction()
elif prompt == "E":
    confirmSub = input('Are you sure you want to quit \nPress Y for Yes or N for no')
    if confirmSub == 'Y':
    	quit()
    elif confirmSub == 'N':
    	getOption = input('Start a new transaction')
