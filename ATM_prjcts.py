from hmac import new
import time
print("\n\n*********************\tWelcome to ABC Bank.\t*********************\n\nPlease Insert Your Card\n\n")
time.sleep(5)
Account_Balance = 4000
password = 1232
pin = int(input("Enter Your PIN: "))

if pin == password:
    while True:
        print ("""
            1 == Balance
            2 == Withdraw
            3 == Deposit
            4 == History
            5 == Quit
            """)
        try:
            option = int(input("Please Enter Your Choice: "))
        except:
            print("Please Enter Valid Value.")

        if option == 1:
            print(f"Your Current Balance is {Account_Balance}.")
            prim_bal = Account_Balance
        if option == 2:
            withdrawl_amount = int(input("Please Enter The Withdrawl Amount: Rs."))
            if withdrawl_amount > Account_Balance:
                print("Invalid Amount! Please Try Again.")
            elif withdrawl_amount <= Account_Balance:
                    Account_Balance = Account_Balance - withdrawl_amount
                    print(f"Rs.{withdrawl_amount} is Debited from Your Account.")
                    print(f"Your Current Account Balance is: Rs.{Account_Balance}.")
            deb_bal = Account_Balance
        if option == 3:
            deposit = int(input("Please Enter Deposit Amount: Rs."))
            Account_Balance = Account_Balance + deposit
            print(f"Rs.{deposit} is Deposited to Your Account.")
            print(f" Your Current Account Balance is: Rs.{Account_Balance}")
            cred_bal = Account_Balance
        if option == 4:
            print(prim_bal)
            print("Debited", withdrawl_amount, "Balance Amount is: ", deb_bal)
            print("Credited", deposit, "Balance Amount is: ", cred_bal)
        if option == 5:
            time.sleep(2)
            break
else:
    print("PIN Incorrect!!! Try Again.")