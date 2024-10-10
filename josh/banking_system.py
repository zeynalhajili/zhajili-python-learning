# # Task: Enhanced Banking System Simulation

# Create a Customer Class:
# Attributes: (done)
        # name: The name of the customer (string).
        # age: The age of the customer (integer).
        # accounts: A list to hold multiple accounts (initially an empty list).
        # transaction_history: A list to store transaction records (initially an empty list).
# Methods: (in progress)
        # add_account(account_number): Method to add a new account (account number) to the customer's account list.
        # view_accounts(): Method to display all accounts associated with the customer.
        # deposit(account_number, amount): Method to deposit money into a specified account. If the account exists, increase the balance and record the transaction.
        # withdraw(account_number, amount): Method to withdraw money from a specified account. Ensure sufficient balance, then decrease the balance and record the transaction.
        # view_transaction_history(): Method to display the transaction history for the customer.
        
# Create a Bank Class:
# Attributes:
        # customers: A list to hold multiple Customer objects (initially an empty list).
# Methods:
        # add_customer(customer): Method to add a new customer to the bank’s customer list.
        # find_customer(name): Method to find a customer by their name and return their object.
        # transfer_funds(account_from, account_to, amount): Method to transfer funds between two accounts. Ensure sufficient balance and update both accounts accordingly.
        # view_all_accounts(): Method to view all accounts and their balances within the bank.
        
# User Interaction:
# Implement a menu-driven interface that allows users to:
    # Add a new customer.
    # Add a new account to an existing customer.
    # Deposit funds into an account.
    # Withdraw funds from an account.
    # Transfer funds between accounts.
    # View customer details (including accounts and transaction history).
    # Exit the program.
# Use a loop to display the menu repeatedly until the user chooses to exit.

# Transaction Records:
# Each transaction (deposit, withdrawal, and transfer) should be recorded in the transaction_history attribute of the Customer class. The transaction record should include:
    # Date and time of the transaction.
    # Type of transaction (Deposit, Withdrawal, Transfer).
    # Amount involved.
    # Account number.
    
# Data Validation:
# Ensure that:
    # The account number is unique when adding a new account.
    # A withdrawal cannot exceed the available balance.
    # Fund transfers cannot occur between accounts of different customers directly, but customers can transfer between their own accounts.
    
# Additional Features to Consider:
    # Implement error handling for invalid inputs (e.g., non-numeric input for deposits/withdrawals).
    # Allow customers to have multiple accounts with different balances.
    # Optionally, implement a feature to save and load customer data from a file (for future practice with file I/O).
    

class Customer():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.accounts = []
        self.transaction_history = []
        
    def add_account(self,account_number, balance=0):
        #template for account
        account = {
            "account_number": account_number,
            "balance": balance
        }
        
        self.accounts.append(account)
        return self.accounts
    
    def view_accounts(self):
        return self.accounts
       
    def deposit(self,account_number,amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return # I will stop here even amount is negative is 0, could be checked furhther with adding loop.
        for account in self.accounts:
            if account_number == account['account_number']:
                print("Account exists, balance will be updated!")
                account["balance"] = account["balance"] + amount
                return

        print("Account is new, creating account and updating balance!")
        new_account = {
        "account_number": account_number,
        "balance": amount  
                        }
        self.accounts.append(new_account)       
        return self.accounts 
    
    # def withdraw(self,account_number, amount):
                           
            

customer1 = Customer("Zeynal", 33)
customer2 = Customer("Faraj", 8)
customer3 = Customer("Ronaldo", 39)

customer1.add_account(2011)
customer2.add_account(2042)
customer3.add_account(2023)
customer2.add_account(2004)

customer2.deposit(2004,1119)
print(customer2.view_accounts())