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
