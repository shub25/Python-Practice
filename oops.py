class Atm:
    def __init__(self):
        print("Welcome to ATM")
        self.__pin = ""
        self.__balance = 0.0


sbi=Atm()
sbi.__pin = "1234"
sbi.__balance = 1000.0
print("Your ATM pin is:", sbi.__pin)
print("Your ATM balance is:", sbi.__balance)
print(sbi._Atm__pin)  # Accessing private variable using name mangling
print(sbi._Atm__balance)  # Accessing private variable using name mangling