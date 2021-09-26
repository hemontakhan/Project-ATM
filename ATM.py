class atm(object):
    def __init__(self,name,bankname,pinnumber,cardnumber):
        self.name = name
        self.bankname = bankname
        self.pinnumber = pinnumber
        self.cardnumber = cardnumber

    def CashWithDrawl(self):
         amount = input('Enter The amount :-')
         print(amount)
    
    def BalanceEnquiry(self):
        print('Your Present Balance is - 1,50,00,000')

 
sbi = atm('Ayush Khan','Indusind Bank',2607,726157890)
print(sbi.name)
print(sbi.bankname)
print(sbi.pinnumber)
print(sbi.cardnumber)
print(sbi.CashWithDrawl())
print(sbi.BalanceEnquiry())
