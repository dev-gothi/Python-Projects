# MAKING ATM SYSTEM WITH USING CLASS


class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        

    def menu(self):
        while (True):
            userinput = input("""
                            Hello Welcome to our Atm System
                            1 . SetPin
                            2 . CheckBalance
                            3 . Deposit
                            4 . Withdraw
                            5 . Exit
            """)
            if (userinput == "1"):
                self.SetPin()
            elif (userinput == "2"):
                self.CheckBalance()
            elif (userinput == "3"):
                self.Deposit()
            elif (userinput == "4"):
                self.Withdraw()
            elif (userinput == "5"):
                print("ThankYou")
                break
            else:
              print("Invalid Choice Try Again")

    def SetPin(self):
        self.pin = input("Enter your pin : ")
        print("Pin set successfully")

    def CheckBalance(self):
        temp = input("Enter Pin : ")
        if (temp == self.pin):
            print(self.balance)
        else:
            print("Invalid pin")

    def Deposit(self):
        temp = input("Enter Pin : ")
        if (temp == self.pin):
            amount = int(input("Enter Amount "))
            self.balance = self.balance + amount
        else:
            print("Invalid Pin")

    def Withdraw(self):
        temp = input("Enter Pin :")
        if (temp == self.pin):
            amount = int(input("Enter Amount "))
            if (self.balance >= amount):
                self.balance = self.balance - amount
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Pin")


sbi = Atm()
# sbi.CheckBalance()
hdfc = Atm()
hdfc.menu()
