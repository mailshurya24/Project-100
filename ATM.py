class Atm:
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def checkBalance(self):
        print("Your balance is $50000")

    def withdrawal(self, amount):
        newAmount = 50000 - amount
        print("Congratulations! You have withdrawn $"+str(amount) +". Your remaining balance is $"+ str(newAmount)+".")


def main():
    cardNo = input("Insert your card number:- ")
    pinNo  = input("Enter your pin number:- ")

    newUser =  Atm(cardNo, pinNo)

    print("Choose your activity:")
    print("1. Balance Enquiry")
    print("2. Withdrawal")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        newUser.checkBalance()
    elif (activity == 2):
        amount = int(input("Enter the amount:- "))
        newUser.withdrawal(amount)
    else:
        print("Please enter a valid number")


main()