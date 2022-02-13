from email import charset
from xml.dom.minidom import CharacterData


class Atm:
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def balanceInquiry(self):
        print('Your balance is: $500')

    def cashWithdrawal(self, amount):
        latest_amount = 500-amount
        print('You withdrawed: $' + str(amount) +
              ' Your remaining balance is: $' + str(latest_amount))


def main():
    name = charset(input('Please enter your name: '))
    print('Welcome, ' + name)

    cn = int(input('Please enter your card number: '))

    pn = int(input(' Please enter your pin: '))
    current_user = Atm(cn, pn)

    print('Select Transaction:')
    print('1: Balance Inquiry')
    print('2: Cash Withdrawal')
    transaction = int(input('Select transaction choice: '))

    if(transaction == 1):
        current_user.balanceInquiry()
    elif(transaction == 2):
        amount = int(input('Enter amount: '))
        current_user.cashWithdrawal(amount)
    else:
        print('Kindly enter a valid option(number)')


if __name__ == '__main__':
    main()
