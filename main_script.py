import logging

logging.basicConfig(filename='bankAccount.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class Account:
    num_of_accounts = 0
    def __init__(self,first,last,acountnum,balance,credit_line=1500):
        self.first = first
        self.last = last
        self.acountnum = acountnum
        self.Balance = balance
        self.credit_line = credit_line
        Account.num_of_accounts += 1

        logging.info("Created Account:{} - {}".format(self.fullname,self.acountnum))

    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)

    @fullname.setter
    def fullname(self,string):
        """ setter property gets the fullname and 
        updates the first and last name of the person
        first,last = string.split(' ')
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first,self.last)

    @classmethod
    def from_string(cls,string):
        """creates a new account object with the account details 
        in a string argument
        """
        
        first,last,acountnum,Balance,credit_line = string.split('-')
        logging.info("Created Account:{} {} - {}".format(first,last,acountnum))
        return cls(first,last,int(acountnum),int(Balance),credit_line)

    def withdraw(self,amount):
        if (self.Balance - amount) < -self.credit_line:
            return False
        else:
            self.Balance -= amount
            return True

    def deposit(self,amount):
        self.Balance += amount
        return True

    def transfer(self,other,amount):
        if (self.Balance - amount) < -self.credit_line:
            return False
        else:
            self.Balance -= amount
            other.Balance += amount
            return True

    def balance(self):
        return self.Balance
    
    def getaccountnum(self):
        return self.acountnum
    
    def getcreditline(self):
        return self.credit_line

acnt_obj1 = Account('mohd','shoaib',6787345,10000)
acnt_obj2 = Account('eric','donald',5645787,20000)
acnt_obj3 = Account.from_string('mds-kabeer-673452-30000-1500')

print(acnt_obj1.balance())
print(acnt_obj1.fullname)
print(acnt_obj1.email)
print(Account.num_of_accounts)
