class ATM(object):
    def __init__(self, ATM_Card_Number, Pin_Number, Balance):
        self.ATM_Card_Number=ATM_Card_Number
        self.Pin_Number=Pin_Number
        print("Card Number = "+str(self.ATM_Card_Number))
        print("Pin = "+str(self.Pin_Number))
        self.Balance = int(Balance)
    def deposite(self, Deposit):
        self.Balance = self.Balance + int(Deposit)
        print("Cash Withrawed " +str(deposite)+ ", Balance = " +str(self.Balance))
    def cashWithdrawl(self, cashWithdrawl):
        self.Balance = self.Balance - int(cashWithdrawl)
        print("Cash Withrawed " +str(cashWithdrawl)+ ", Balance = " +str(self.Balance))
        
    def balanceEnquiry(self):
        print("Your balance = "+str(self.Balance))

Card_Number = input("Enter Your Card Number :- ")
Pin = input("Enter Your Pin :- ")
Transaction1 = ATM(Card_Number, Pin, 0)

Start = True
while(Start):
    Choice  = input("\n1 - Deposit, 2 - Withdrawl, 3 - Balance, 4 - Exit.\nEnter Your Choice :- ")
    if(Choice == "1"):
        deposite = input("\nEnter cash to be deposited :- ")
        Transaction1.deposite(deposite)
    elif(Choice == "2"):
        withdraw = input("\nEnter cash to be withrawed :- ")
        Transaction1.cashWithdrawl(withdraw)
    elif(Choice == "3"):
        Transaction1.balanceEnquiry()
    elif(Choice == "4"):
        Start = False
    else:
        print("\n-_- Eye Checkup !!!")