casino_vault=100000
#This function for rolling the dices
#And giving the prize accordingly
def roll(a): #a is the argument as the bet
    casino_vault+=a
    bet=a 
    print('Roll')
    import random # import thre random function
    dice1=int(random.randint(1,6))# To give each dice
    dice2=int(random.randint(1,6))# a random value
    print('DICE1\t\t\t',dice1,'\nDICE2\t\t\t',dice2)
    #the following codes are to judge whether 
    #the combination of the dices can win a prize
    if dice1==1 and dice2==1:
        print(format('\tSnake Eyes'))
        prize=10*bet
        print('\tPRIZE: ',format(prize,',.2f'),'$',sep='')
        casino_vault-=prize
        print('casino vault: ',format(casino_vault,',.2f'),'$',sep='')
        return prize
    elif dice1==2 and dice2==2:
        print(format('\tHard Four'))
        prize=3*bet
        print('\tPRIZE: ',format(prize,',.2f'),'$',sep='')
        casino_vault-=prize
        print('casino vault: ',format(casino_vault,',.2f'),'$',sep='')
        return prize
    elif dice1==3 and dice2==3:
        print(format('\tHard Six'))
        prize=3*bet
        print('\tPRIZE: ',format(prize,',.2f'),'$',sep='')
        casino_vault-=prize
        print('casino vault: ',format(casino_vault,',.2f'),'$',sep='')
        return prize
    elif dice1+dice2==4:
        print(format('\tEasy Four'))
        prize=1.5*bet
        print('\tPRIZE: ',format(prize,',.2f'),'$',sep='')
        casino_vault-=prize
        print('casino vault: ',format(casino_vault,',.2f'),'$',sep='')
        return prize
    elif dice1+dice2==6:
        print(format('\tEasy Six'))
        prize=1.5*bet
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
    print('         This is a slot machine')
    print(' The casio have a million dollar in its vault')
    print('You can win this game by making the casino bankrupt')
    print('          1$ per roll')
    print('             PRIZE              ')
    print('Snake Eyes   1 and 1     10.00$')
    print('Hard Four    2 and 2      3.00$')
    print('Hard Six     3 and 3      3.00$')
    print('Easy Four    4 in total   1.50$')
    print('Easy Six     6 in total   1.50$')
    print('===============================')

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

#This function is to make sure that the bet input
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

def main():
    #a is a sentinel deciding telling the program
    #which case it is
    a=''
    #call the instrucion()
    instruction()
    #set default money
    default_money=10
    #let user enter a balance
    money=input('Enter your balance(DEFAULT 10$)\n')
    money=valid(money,default_money)
    #set default bet
    default_bet=1
    #let user enter a bet
    bet=input('Enter your bet(DEFAULT 1):\n')
    bet=valid1(bet,default_bet,money)

    #loop
    while not a=='x':
        #case1: using the old bet and roll again
        if a=='':
            if money>=bet:
                money-=1*bet
                print('==========================')
                money+=roll(bet)
                print('')
                print('Your balance: ',format(money,',.2f'),'$',sep='')
                print('')
                #different value of a can allow user
                #to roll again with the same bet;
                #change the bet and roll again;
                #or exit the game
                a=input('1)Press ENTER to roll again\n\
2)enter new bet\n\
3)enter x to cash your balance\n')
          #case2: You run out of money or the current bet is too big
            else:
                if money==0:
                    #let user to decide
                    option=input('You do not have enough money for a roll\nenter a to add money\nenter x to exit\n')
                    #entering a: add money to his or her balance
                    if option=='a':
                        add=valid(input('How much money do you want to add\n'),0)
                        money+=add
                    #entering anything else: exit the game
                    else:
                        a='x'
                else:
                    #let user to decide
                    option=input('You do not have enough money for a roll\nenter a to add money\nenter b to change bet\nenter x to exit\n')
                    #entering a: add money to his or her balance
                    if option=='a':
                        add=valid(input('How much money do you want to add\n'),0)
                        money+=add
                    #entering b: change the bet
                    elif option=='b':
                        bet=input('Enter your bet(DEFAULT 1)\n')
                        bet=valid1(bet,default_bet,money)
                    #entering anything else: exit the game
                    else:
                        a='x'
                
                
       #case3: user change a bet
        else:
            bet=valid1(a,default_bet,money)
            money-=1*bet
            print('==========================')
            money+=roll(bet)
            print('')
            print('Your balance: ',format(money,',.2f'),'$',sep='')
            print('')
            a=input('1)Press ENTER to roll again\n\
2)enter new bet\n\
3)enter x to cash your balance\n')
    #tell the user that the game is over           
    print('*****************GAME OVER*****************')
    #Print the flithy bill
    money_printer(money)
    


#call the main function
main()

#How to prevent bad input like letters?
#improve the prize mechanism
#allow user to add money when they are playing
