#Using Basic OOP(Object oriented programming) to mimic bank transactions.

class bank:
    bankname="Uni Bank"
    branch="Riverside,London"

    #Create account
    def __init__(self, username, ccv, address):
        self.username=username
        self.ccv=ccv
        self.address=address
        self.balance=0.0


    #depoist
    def deposit(self,amount):
         self.balance=self.balance+amount
         print(f'{amount} deposited successfully')

    #withdraw
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            print(f'{amount} withdraw successfully')
        else:
            print('Insufficent Fund...')

    #ministatement
    def ministatement(self):
        print(f'Your account balance is {self.balance}')


print(f'Welcome to {bank.bankname} , {bank.branch}')

#collect user data for account creation
username=input('Enter Your name :')
ccv=input('Enter ccv card number : ')
address=input('Enter Your address : ')

#FIX THIS PART
#while True:
    #if username == str(" "):
        #print("Key in name please")
    #elif ccv == int():
        #print("Key in ccv number kindly, 3 digit number behind card")
    #elif address == str(" "):
        #print("Key in address please")
    #else:
        #break


b=bank(username,ccv,address) # object creation based on user provided data

#Creating select option
while True:
    print('\nPlease Select any Option : ')
    print('1.Deposit\n2.Withdraw\n3.Ministatement\n4.Stop')
    option=int(input(' '))

    if option==1:
        amount=float(input('Enter Deposited amount : '))
        b.deposit(amount)

    elif option==2:
        amount=float(input('Enter Withdraw amount : '))
        b.withdraw(amount)

    elif option==3:
        b.ministatement()

    elif option==4:
        print('Thanks for Trusting Uni Bank, have a great day. ')
        break
    else:
        print('Invalid Option plz select a  valid option')


