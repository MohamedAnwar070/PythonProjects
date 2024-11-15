accounts={}

def open_account():
    print("----Open A New Account----")
    num_customers=int(input("Number Of Customers : "))
    for i in range(num_customers):
        cusname=input("Input Fullname : ")
        cuspin=int(input("Please Input A Pin Of Your Choice : "))
        cusdeposit=int(input("Please Input A Value To Deposit To Start An Account : "))
        accounts[cuspin]={'Name':cusname,'Balance':cusdeposit}
        print(f"{cusname} Your Account Was Created")
        print(f"Procees Done. Money Deposited Rs.{cusdeposit}")

def withdraw_money():
    print("----Withdraw Money----")
    cuspin=int(input("Enter Your Pin : "))
    if cuspin in accounts:
        amount=int(input("Enter A Amount To Withdraw : "))
        if accounts[cuspin]['Balance'] >=amount:
          accounts[cuspin]['Balance'] -=amount
          print(f"Withdrawel Successfull. New Balance: Rs.{accounts[cuspin]['Balance']}")
        else:
             print("Insufficient Balance")
    else:
        print("Invalid Pin")

def deposit_money():
    print("---Deposit Money----")
    cuspin=int(input("Enter Your Pin : "))
    if cuspin in accounts:
        amount=int(input("Enter A Amount To Deposit : "))
        accounts[cuspin]['Balance'] +=amount
        print(f"Deposit Successful. New Balance: Rs.{accounts[cuspin]['Balance']}")
    else:
        print("Invalid Pin")

def Check_Customers_balance():
    print("----Balance Check----")
    cuspin=int(input("Enter A Pin : "))
    for pin, info in accounts.items():
        print(f"Customer: {info['Name']}, Balance: Rs.{info['Balance']}")

def main():
    while True:
     print("===========================================")
     print("----Welcome To Times Bank----")
     print("*******************************************")
     print("=<< 1. Open A New Account        >>=")
     print("=<< 2. Withdraw Money            >>=")
     print("=<< 3. Deposit Money             >>=")
     print("=<< 4. Check Customers & Balance >>=")
     print("=<< 5. Exit/Quit                 >>=")
    
     choice=int(input("Select Your Choice From The Above Menu : ")  
     if choice==1:
        open_account()
     elif choice==2:
        withdraw_money()
     elif choice==3:
        deposit_money()
     elif choice==4:
        Check_Customers_balance()
     elif choice==5:
        print("Thanks Using Our Bank")
        break
     else:
        print("Invalid Selection!,Please Select Between Number 1 to 5")
main()                                   

#Coded By ANWAR
