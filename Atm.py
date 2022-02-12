class Atm:
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def balanceInquiry(self):
        print('your balance is: $500')

    def cashWithdrawal(self, amount):
        latest_amount = 500-amount
        print('you withdrawed: $' + str(amount) +
              ' your remaining balance is: $' + str(latest_amount))


def main():
    name = input('please enter your name: ')
    print('welcome, ' + name)
    cn = input('enter your card number: ')
    pn = input(' please enter your pin: ')
    current_user = Atm(cn, pn)

    print('select transaction:')
    print('1: Balance Inquiry')
    print('2: Cash Withdrawal')
    transaction = int(input('select transaction choice: '))

    if(transaction == 1):
        current_user.balanceInquiry()
    elif(transaction == 2):
        amount = int(input('enter amount: '))
        current_user.cashWithdrawal(amount)
    else:
        print('kindly enter a valid option(number)')


if __name__ == '__main__':
    main()
