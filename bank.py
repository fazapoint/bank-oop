# Customer Class
class Customer:

    def __init__ (self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance
        self.depositHistory = []
        self.withdrawHistory = []
    
    def checkUsername(self):
        return self.username
    
    def checkPassword(self):
        return self.password
    
    def checkBalance(self):
        return self.balance

    def withdrawBalance(self, amount):
        self.balance -= amount
        self.withdrawHistory.append(f"Withdraw Rp.{amount}")
    
    def depositBalance(self, amount):
        self.balance += amount
        self.depositHistory.append(f"Deposit Rp.{amount}")

    def checkDepositHistory(self):
        return self.depositHistory

    def checkWithdrawHistory(self):
        return self.withdrawHistory


customers = []
currentCustomer = None

def login_menu():
    global customers, currentCustomer
    print("### Login ###")
    # login with username and password
    usernameInput = input("Input Username : ")
    passwordInput = input("Input password : ")
    
    
    for customer in customers:
        if customer.checkUsername() == usernameInput and customer.checkPassword() == passwordInput:
            currentCustomer = customer
            print("LOGIN SUCCESS")
            press_any_key()
            return True 
    print("LOGIN FAILED")
    press_any_key()

def logout_menu():
    global currentCustomer
    currentCustomer = None
    print("LOGGED OUT")
    press_any_key()

def createAccount_menu():
    global customers
    # create username and password
    newUsername = input("Create Username : ")
    newPassword = input("Create a Password : ")
    initialDeposit = int(input("First Deposit : Rp."))

    # check if username already exist
    for customer in customers:
        if customer.checkUsername() == newUsername:
            messageFail = print("USERNAME IS CURRENTLY TAKEN!")
            press_any_key()
            return messageFail

    customer = Customer(newUsername, newPassword, initialDeposit)
    customers.append(customer)
    print("REGISTER ACCOUNT SUCCESS")
    press_any_key()


def deposit_menu():
    global currentCustomer
    depositAmount = int(input("Insert deposit's amount: Rp."))
    confirm_deposit = input(f"Are you sure want to deposit Rp.{depositAmount}? [y/n] : ").lower()
    if confirm_deposit == 'y':
        currentCustomer.depositBalance(depositAmount)
        print("DEPOSIT SUCCESS")
    elif confirm_deposit == 'n':
        print("DEPOSIT CANCELED")
    else:
        print("PLEASE INPUT VALID OPTION")
    press_any_key()

def checkBalance_menu():
    global currentCustomer
    checkBalance = f"Your ({currentCustomer.checkUsername()}) BALANCE : Rp.{currentCustomer.checkBalance()}"
    print(checkBalance)
    press_any_key()

def withdraw_menu():
    global currentCustomer
    withdraw_amount = int(input("Insert withdraw's amount: Rp."))
    if withdraw_amount > currentCustomer.checkBalance():
        print("NOT ENOUGH BALANCE TO WITHDRAW")
        press_any_key()
    else:
        currentCustomer.withdrawBalance(withdraw_amount)
        print("WITHDRAW SUCCESS")
        press_any_key()

def viewTransactionsHistory_menu():
    global currentCustomer
    print("### Deposit History ###")
    for depositHistory in currentCustomer.checkDepositHistory():
        print(f"- {depositHistory}")
    
    print("### Withdraw History ###")
    for withdrawHistory in currentCustomer.checkWithdrawHistory():
        print(f"- {withdrawHistory}")
            

    press_any_key()

def showAllCustomers_menu():
    print("### Customers list ###")
    for customer in customers:
        print(f"username : {customer.checkUsername()} | password : {customer.checkPassword()}")
    press_any_key()
    

def press_any_key():
    print("===========================")
    input("Press any key to continue...")


while True:
    # Menu Before Login
    if currentCustomer == None:
        print("### Welcome to XBank Please Login or Register ###")
        print("1. Login")
        print("2. Create an Account")
        print("3. Show all customers (admin)")
        
        select_menu = input("Choose Menu : ")
        if select_menu == '1':
            login_menu()
        elif select_menu == '2':
            createAccount_menu()
        elif select_menu == '3':
            showAllCustomers_menu()
        else:
            print("PLEASE INPUT VALID OPTION")
            press_any_key()
    # Menu After Login
    else:
        print(f"### Welcome to XBank {currentCustomer.checkUsername()}! ###")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transactions History")
        print("5. Logout")
        select_menu = input("Choose Menu : ")

        if select_menu == '1':
            deposit_menu()
        elif select_menu == '2':
            withdraw_menu()
        elif select_menu == '3':
            checkBalance_menu()
        elif select_menu == '4':
            viewTransactionsHistory_menu()
        elif select_menu == '5':
            logout_menu()
        else:
            print("PLEASE INPUT VALID OPTION")
            press_any_key()
    

