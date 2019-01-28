import unittest
from BankAccount import Account

##unit testing for the Bank account code

class TestAccount(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setupclass")
        
    @classmethod
    def tearDownClass(cls):
        print("teardownclass")

    def setUp(self):
        self.acnt_obj1 = Account('mohd', 'shoaib', 6787345, 10000)
        self.acnt_obj2 = Account('eric', 'donald', 5645787, 20000)

    def tearDown(self):
        print("teardown\n")

    def test_full_name(self):
        print("running test case test_full_name")
        self.assertEqual(self.acnt_obj1.fullname,'mohd shoaib')
        self.assertEqual(self.acnt_obj2.fullname,'eric donald')

        self.acnt_obj1.first = "mohammed"
        self.acnt_obj2.first = "mac"

        self.assertEqual(self.acnt_obj1.fullname,'mohammed shoaib')
        self.assertEqual(self.acnt_obj2.fullname,'mac donald')

    def test_email(self):
        print("running test case test_email")
        self.assertEqual(self.acnt_obj1.email,'mohd.shoaib@gmail.com')
        self.assertEqual(self.acnt_obj2.email,'eric.donald@gmail.com')

        self.acnt_obj1.first = "mohammed"
        self.acnt_obj2.first = "mac"

        self.assertEqual(self.acnt_obj1.email,'mohammed.shoaib@gmail.com')
        self.assertEqual(self.acnt_obj2.email,'mac.donald@gmail.com')

    def test_withdraw(self):
        print("running test case test_withdraw")
        print("running test case test_full_name")
        self.assertEqual(self.acnt_obj1.Balance, 10000)
        self.assertEqual(self.acnt_obj2.Balance, 20000)

        balance = self.acnt_obj1.withdraw(5000)
        balance2 = self.acnt_obj2.withdraw(5000)

        self.assertEqual(balance, True)
        self.assertEqual(balance2, True)

    def test_deposit(self):
        print("running test case test_deposit")
        self.assertEqual(self.acnt_obj1.Balance, 10000)
        self.assertEqual(self.acnt_obj2.Balance, 20000)

        Depos = self.acnt_obj1.deposit(5000)
        Depos2 = self.acnt_obj2.deposit(5000)

        self.assertEqual(Depos,True)
        self.assertEqual(Depos2,True)

    def test_transfer(self):
        print("running test case test_transfer")
        self.assertEqual(self.acnt_obj1.Balance, 10000)

        trans = self.acnt_obj1.transfer(self.acnt_obj2,5000)

        self.assertEqual(trans, True)

    def test_balance(self):
        print("running test case test_balance")
        self.assertEqual(self.acnt_obj1.Balance, 10000)
        self.assertEqual(self.acnt_obj2.Balance, 20000)

        balan = self.acnt_obj1.balance()
        balan2 = self.acnt_obj2.balance()

        self.assertEqual(balan,10000)
        self.assertEqual(balan2,20000)

if __name__ == '__main__':
    unittest.main()
