import random
database = {}


#Initialization function#

def init(): 
    print('Welcome to EQUITY--BANK')
    checkAccount= int(input('Do you have an account: 1 (YES) 2 (NO ) \n'))
    if (checkAccount==1):
        login()
    elif (checkAccount==2):
        print(register())
    else:
        print('Invalid option selected')
        init()



    #LOGIN FUNCTION 
def login():
    print('>>>>> Login Into Your Account <<<<<')
    userAccount = int(input('Enter your Account Number \n'))
    password = input ('Enter Your Password \n')

    for accountNumber,userDetails in database.items():
        if(accountNumber == userAccount):
            if (userDetails[3] == password):
                bankOperation()
            else:
                print('Wrong Account or Password')  
                login()



#USER REGISTRATION FUNCTION FOR NEW USERS
#ACCOUNT NUMBER GENERATOR
def register():

    print(' ***** Register as a New User *****')

    email = input('Enter Your Email Address \n')
    first_name = input('Enter Your First Name \n')
    last_name = input('Enter Your Last Name \n')
    password = input('Create Your Password \n')

    accountNumber = generateAccount()

    database[accountNumber] = [first_name, last_name, email, password ]

    print('Account Created Succesful')
    print('########## ##### #########')
    print('Your Account Number is : %d' % accountNumber)
    print('Keep Your Account Number Safe')
    print('########## ##### #########')

    login()




#OPERATIONAL FUNCTIONALITY

def bankOperation():
    print('======= WELCOME ========')

    print('Please choose what you want to do next')

    print('1 --- withdrawal')
    print('2 --- Deposit')
    print('3 --- Transfer')
    print('4 --- logout')
    print('5 --- Exit' )

    choice = input()

    if choice == '1':
        withdrawal()
    elif choice == '2':
        deposit()
    elif choice == '3':
        transfer()
    elif choice == '4':
        login()
    elif choice == '5':
        exit()
    else:
        print('Invalid option selected')
        bankOperation()


#WITHDRAWAL FUNCTION
def withdrawal():
    print('How much would you like to withdraw ')
    amount = int(input())
    print('You are aboutto Withdraw %d' %amount + ' Naira')
    confirm= int(input('1 (YES) 2 (NO ) \n'))
    if (confirm==1):
        print('You have Withdrawn %d ' % amount + ' Naira')
        print('Please Take Your Cash \n\n')
        anotherOperation()  

    elif (confirm==2): 
            withdrawal()
    else:
        print('Invalid option selected')
        login()


#DEPOSIT FUNCTION 
def deposit():
    print('How much would you like to deposit ')
    depositfund = int(input())
    print('You are about to Deposit %d' % depositfund + ' Naira')
    confirm= int(input('1 (YES) 2 (NO ) \n'))
    if (confirm==1):
        print('You have Deposited %d ' % depositfund + ' Naira \n')
        print('######  THANK YOU FOR BANKING WITH US  ###### \n\n ')
        anotherOperation()

    elif (confirm==2): 
            bankOperation()
    else:
        print('Invalid option selected')
        login()

#TRANSFER FUNCTION
def transfer():
    accountNumber = generateAccount()
    print('How much would you like to Transfer ') 
    transferfund = int(input())
    print('You are About to Transfer %d' %transferfund + ' to %d' %accountNumber +' Naira \n')
    confirm= int(input('1 (YES) 2 (NO ) \n'))
    if (confirm==1):
        print('Transfer Completes \n')
        print('######  THANK YOU FOR BANKING WITH US  ###### \n\n')
        anotherOperation()

    elif (confirm==2): 
            bankOperation()
    else:
        print('Invalid option selected')
        login()

#FUNCTION TO PERFORM ANOTHER OPERATION 
def anotherOperation():
    print('Would you Like to Perform Another Transaction')
    option= int(input('1 (YES) 2 (NO ) \n'))
    if(option==1):
        bankOperation()
    elif(option==2):
            exit()
    else:
        print('Invalid option selected')
        login()

#FUNCTION TO GENERATE ACCOUNT NUMBER RANDOMLY
def generateAccount():
    return random.randrange(1111111111,9999999999)



#### ACTUAL BANKING SYSTEM ####

init()
