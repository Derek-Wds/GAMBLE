def read():
    k=open('/Users/lihongyi/Desktop/Vault.txt')
    casino_vault=float(k.read())
    k.close()
    global casino_vault
#This function for rolling the dices
#And giving the prize accordingly
def roll(a): #a is the argument as the multiplier
    casino_vault+=a
    multiplier=a
    print('Roll')
    import random # import thre random function
    dice1=int(random.randint(1,6))# To give each dice
    dice2=int(random.randint(1,6))# a random value
    print('DICE1\t\t\t',dice1,'\nDICE2\t\t\t',dice2)
    #the following codes are to judge whether
    #the combination of the dices can win a prize
    if dice1==1 and dice2==1:
        print(format('\tSnake Eyes'))
        prize=10*multiplier
        print('\tPRIZE: ',format(prize,',.2f'),'$',sep='')
        casino_vault-=prize
        print('casino vault: ',format(casino_vault,',.2f'),'$',sep='')
        return prize
    elif dice1==2 and dice2==2:
        print(format('\tHard Four'))
        prize=3*multiplier
        print('\tPRIZE: ',format(prize,',.2f'),'$',sep='')
        casino_vault-=prize
        print('casino vault: ',format(casino_vault,',.2f'),'$',sep='')
        return prize
    elif dice1==3 and dice2==3:
        print(format('\tHard Six'))
        prize=3*multiplier
        print('\tPRIZE: ',format(prize,',.2f'),'$',sep='')
        casino_vault-=prize
        print('casino vault: ',format(casino_vault,',.2f'),'$',sep='')
        return prize
    elif dice1+dice2==4:
        print(format('\tEasy Four'))
        prize=2*multiplier
        print('\tPRIZE: ',format(prize,',.2f'),'$',sep='')
        casino_vault-=prize
        print('casino vault: ',format(casino_vault,',.2f'),'$',sep='')
        return prize
    elif dice1+dice2==6:
        print(format('\tEasy Six'))
        prize=1*multiplier
        print('\tPRIZE: ',format(prize,',.2f'),'$',sep='')
        casino_vault-=prize
        print('casino vault: ',format(casino_vault,',.2f'),'$',sep='')
        return prize
    else:
        print("")
        print('casino vault: ',format(casino_vault,',.2f'),'$',sep='')
        return 0
    global casino_vault

# This function is to explain the rules to the user
def instruction():
    print('     This time you are playing against the casino     ')
    print('  The casino have ',format(casino_vault,',.2f'), '$ dollar in its vault',sep='')
    print('  You can win this game by making the casino bankrupt')
    print('           Your balance is 1,000,000.00 $')
    print('                     1$ per roll')
    print('                        PRIZE              ')
    print('          Snake Eyes   1 and 1     10.00$')
    print('          Hard Four    2 and 2      3.00$')
    print('          Hard Six     3 and 3      3.00$')
    print('          Easy Four    4 in total   2.00$')
    print('          Easy Six     6 in total   1.00$')
    print('          ===============================')
    print('                      Good luck!')

#This function is to make sure the money input
# is a positive floating point
def valid(value,default):
    if value=='':
        value=default
    value=float(value)
    while not value>0:
        value=float(input('It must be lager than 0:\n'))
        if value=='':
            value=default
    return value

#This function is to make sure that the multiplier input


#is a positive floating point and no larger than user's balance
def valid1(value,default,money):
    if value=='':
        value=default
    value=float(value)
    while not (value>0 and value<=money) :
        value=float(input('It must be lager than 0 and smaller than or equal to your balance:\n'))
        if value=='':
            value=default
    return value


#This is a function to print a bill
def money_printer(money):
    print('='*43)
    for i in range(1,4):
        print('*'+41*' '+'*')
    print('*'+format(money,'^41,.2f')+'*')
    print('*',format('$','^40')+'*')
    for i in range(1,4):
        print('*'+41*' '+'*')
    print('='*43)
    print('')

def ending_chosing(vault,money):
    if (vault>0 and money>0):
        print('*****************GAME OVER*****************')
        #Print the flithy check
        print("Here's your check\n")
        money_printer(money)
    elif money==0:
        print('*****************GAME OVER*****************')
        print('Oops, casino won all your money...')
    else:
        print('*****************GAME OVER*****************')
        print('Congratulations! You bankrupt the casino!!!')
        #Print the flithy check
        print("Here's your check\n")
        money_printer(money)

def write(casino_vault):
    casino_vault=str(casino_vault)
    k=open('/Users/lihongyi/Desktop/Vault.txt','w')
    k.write(casino_vault)
    k.close()

def score_board(money):
    net=money-1000000
    net='$'+format(net,',.2f')
    print('Your net win is: ',net)
    name=input('Please enter your name\n')
    if name=='':
        name='user'
    lenth=len(name)
    num=23-lenth
    newline='\n'+name+' '*num+net
    file=open('/Users/lihongyi/Desktop/score_board.txt','r+')
    x=file.read()
    x=newline
    file.write(x)
    file.close
    file=open('/Users/lihongyi/Desktop/score_board.txt')
    x=file.read()
    print(format('Score Board','^40'))
    print('='*40)
    print(x)

def main():
    read()
    #a is a sentinel deciding telling the program
    #which case it is
    a=''
    #call the instrucion()
    instruction()
    #let user enter a balance
    money=1000000
    #set default multiplier
    default_multiplier=1
    #let user enter a multiplier
    multiplier=input('Enter your multiplier(DEFAULT 1):\n')
    multiplier=valid1(multiplier,default_multiplier,money)

    #loop
    while not a=='x':
        if casino_vault>0:
            #case1: using the old multiplier and roll again
            if a=='':
                if money>=multiplier:
                    money-=1*multiplier
                    print('==========================')
                    money+=roll(multiplier)
                    print('')
                    print('Your balance: ',format(money,',.2f'),'$',sep='')
                    print('')
                    #different value of a can allow user
                    #to roll again with the same multiplier;
                    #change the multiplier and roll again;
                    #or exit the game
                    a=input('1)Press ENTER to roll again\n\
2)enter new multiplier\n\
3)enter x to cash your balance\n')
                #case2: You run out of money or the current multiplier is too big
                else:
                    if money==0:
                        a='x'
                    else:
                        #let user to decide
                        option=input('You do not have enough money for a roll\n\
1)enter a new multiplier\n\
2)enter x to exit\n')
                        #entering b: change the multiplier
                        if option=='x':
                            a='x'
                        #entering anything else: exit the game
                        else:
                            multiplier=valid1(option,default_multiplier,money)
            #case3: user change a multiplier
            else:
                multiplier=valid1(a,default_multiplier,money)
                money-=1*multiplier
                print('==========================')
                money+=roll(multiplier)
                print('')
                print('Your balance: ',format(money,',.2f'),'$',sep='')
                print('')
                a=input('1)Press ENTER to roll again\n\
2)enter new multiplier\n\
3)enter x to cash your balance\n')
        else:
            a='x'
    ending_chosing(casino_vault,money)
    write(casino_vault)
    score_board(money)



#call the main function
main()

#How to prevent bad input like letters?
#improve the prize mechanism
