class Bank:
    def getdata(self, name, ac_type, ac_num, ac_bal):
        self.name = name
        self.ac_type = ac_type
        self.ac_num = ac_num
        self.ac_bal = ac_bal

    def deposit(self, amount):
        self.ac_bal += amount
        print("Amount deposited successfully.")
        print("Current Balance:", self.ac_bal)

    def withdraw(self, amount):
        if amount > self.ac_bal:
            print("Insufficient balance!")
        elif amount % 100 != 0:
            print("Withdraw amount must be a multiple of 100.")
        else:
            self.ac_bal -= amount
            print(amount, "withdrawn successfully.")
            print("Current Balance:", self.ac_bal)

    def display_balance(self):
        print("Current Balance:", self.ac_bal)


# --- Main Program ---
b1 = Bank()
b1.getdata("Virat", "Savings", 123456789, 50000000)

while True:
    print("\n1. Display Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    ch = int(input("Choose an option: "))

    if ch == 1:
        b1.display_balance()
    elif ch == 2:
        amt = int(input("Enter amount to withdraw: "))
        b1.withdraw(amt)
    elif ch == 3:
        amt = int(input("Enter amount to deposit: "))
        b1.deposit(amt)
    elif ch == 4:
        print("Thank you! Visit again.")
        break
    else:
        print("Invalid choice!")
