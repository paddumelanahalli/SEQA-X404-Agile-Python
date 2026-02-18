class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Error: Deposit must be positive."
        self.balance += amount
        return f"Deposited {amount}. New Balance: {self.balance}"

    def withdraw(self, amount):
        # Intentional Logic Gap: What happens if amount is negative? 
        # Students should find this in testing.
        if amount > self.balance:
            return "Error: Insufficient funds."
        self.balance -= amount
        return f"Withdrew {amount}. New Balance: {self.balance}"

# Example Usage
if __name__ == "__main__":
    my_account = Account("Student_User", 100.0)
    print(my_account.deposit(50))
    print(my_account.withdraw(200)) # Expected Failure

'''
Here is a safer version:

class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            return "Error: Invalid amount type."

        if amount <= 0:
            return "Error: Deposit must be positive."

        self.balance += amount
        return f"Deposited {amount}. New Balance: {self.balance}"

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            return "Error: Invalid amount type."

        if amount <= 0:
            return "Error: Withdrawal must be positive."

        if amount > self.balance:
            return "Error: Insufficient funds."

        self.balance -= amount
        return f"Withdrew {amount}. New Balance: {self.balance}"

    test_inputs = [
    "100",      # string instead of number
    None,       # null value
    [],         # list
    {},         # dictionary
    -50,        # negative withdrawal
    0,          # zero amount
]

Category 2: Boundary Cases
Test	Expected
withdraw(balance)	Allowed
withdraw(balance + 0.01)	Fail
deposit(0)	Fail
withdraw(0)	Fail


    '''

