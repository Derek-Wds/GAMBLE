import random
global odd1,odd2,odd3,p1,p2,p3,p4
odd1=2
odd2=2
odd3=31
p1=10
p2=3
p3=2
p4=1





def read():
    k=open('/Volumes/MAX DRIVE/GAMBLE/LOG/Vault.txt')
    casino_vault=float(k.read())
    k.close()
    return casino_vault

#This function is to make sure that the bet input is valid
def valid1(value,default,money):
    if value=='':
       value=default
    value=str(value)
    while not(value.isdigit()):
        value=input('It must be a non-negative number\n')
    value=float(value)
    while not (value<=money) :
        value=input('It must be smaller than or equal to your balance:\n')
        if value=='':
            value=default
        value=float(value)
    return value

def bet(money,tbet):
    print('='*70)
    if tbet>money:
        print(format('You do not have enough money to place the original bet','^70'))
        print(format('Please place a new bet','^70'))
    default=0
    bet1=valid1(input('Place bet on big(DEFAULT 0)\n'),default,money)
    money-=bet1
    bet2=valid1(input('Place bet on small(DEFAULT 0)\n'),default,money)
    money-=bet2
    bet3=valid1(input('Place bet on triple(DEFAULT 0)\n'),default,money)
    money-=bet3
    tbet=bet1+bet2+bet3

    print('='*70)
    return bet1,bet2,bet3,tbet

def show_bet(bet1,bet2,bet3):
    print('Bet on big:\t',format(bet1,',.2f'),'$',sep='')
    print('Bet on small:\t',format(bet2,',.2f'),'$',sep='')
    print('Bet on triple:\t',format(bet3,',.2f'),'$',sep='')
    print('='*70)

#This function for rolling the dices
#And giving the prize accordingly
def roll1(casino_vault,money,bet1,bet2,bet3,tbet):
    print('Roll')
    dice1=int(random.randint(1,6))# To give each dice
    dice2=int(random.randint(1,6))# a random value
    dice3=int(random.randint(1,6))
    #show the value of each dice
    print('DICE1\t\t\t',dice1,'\nDICE2\t\t\t',dice2,'\nDICE3\t\t\t',dice3)
    total=dice1+dice2+dice3
    #calculate the total and print it
    print('')
    print('The total is',total)
    print('')
    #the following codes are to judge whether
    #the combination of the dices can win a prize
    if (dice1==dice2 and dice1==dice3):
        print('triple win')
        casino_vault-=bet3*odd3
        money+=bet3*odd3
        prize=bet3*odd3
    elif (total>=4 and total<=10):
        print('small win')
        casino_vault-=bet2*odd2
        money+=bet2*odd2
        prize=bet2*odd2
    elif (total>=11 and total<=17):
        print('big win')
        casino_vault-=bet1*odd1
        money+=bet1*odd1
        prize=bet1*odd1
    net=prize-tbet
    print('')
    print('The net win for this bet is \n',format(net,',.2f'),'$',sep='')
    return money, casino_vault


# This function is to explain the rules to the user
def instruction_sic_bo(casino_vault):
    print(format('This is a sic-bo game','^70'))
    print('')
    print(format('Rules','^66'))
    print('='*70)
    print('1)Before you roll, you need to place a bet on big, small and triple')
    print('2)After you roll, the value of the dices will be shown on the screen')
    print('3)Winners will get money accordingly')
    print('4)You have 1,000,000$')
    print('5)You can win this game by bankruptting the casino')
    print('6)The casino have ', format(casino_vault,',.2f'),'$',' in its vault',\
          sep='')
    print('='*70)
    print(format('Betting Option','^66'))
    print('Type\t\t\t\tWager\t\t\t\tOdds')
    print('Big\t\tsum: 11 to 17(except for triple)\t\t',odd1-1, 'to 1')
    print('Small\t\tsum: 4 to 10(except for triple)\t\t\t', odd2-1, 'to 1')
    print('Triple\t\tthree dices have the same value\t\t       ',odd3-1 ,'to 1')



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
            
def ticket_printer():
    print('='*43)
    for i in range(1,5):
        print('*'+41*' '+'*')
    print('*',format('Buffet Ticket','^40')+'*')
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
        print('Oops, the casino took all your money...')
        print('But at least they gave you a buffet ticket!')
        ticket_printer()
    else:
        print('*****************GAME OVER*****************')
        print('Congratulations! You bankrupt the casino!!!')
        #Print the flithy check
        print("Here's your check\n")
        money_printer(money)
    print('')
    print('*'*43)
    print('')

def write(casino_vault):
    casino_vault=str(casino_vault)
    k=open('/Volumes/MAX DRIVE/GAMBLE/LOG/Vault.txt','w')
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
    file=open('/Volumes/MAX DRIVE/GAMBLE/LOG/score_board.txt','r+')
    x=file.read()
    x=newline
    file.write(x)
    file.close
    file=open('/Volumes/MAX DRIVE/GAMBLE/LOG/score_board.txt')
    x=file.read()
    print(format('Score Board','^40'))
    print('='*40)
    print(x)

def roll2(a,casino_vault): #a is the argument as the multiplier
    multiplier=a
    print('Roll')
    dice1=int(random.randint(1,6))# To give each dice
    dice2=int(random.randint(1,6))# a random value
    print('DICE1\t\t\t',dice1,'\nDICE2\t\t\t',dice2)
    #the following codes are to judge whether
    #the combination of the dices can win a prize
    if dice1==1 and dice2==1:
        print(format('\tSnake Eyes'))
        prize=p1*multiplier
        print('\tPRIZE: ',format(prize,',.2f'),'$',sep='')
        casino_vault-=prize
        print('casino vault: ',format(casino_vault,',.2f'),'$',sep='')
        return prize
    elif dice1==2 and dice2==2:
        print(format('\tHard Four'))
        prize=p2*multiplier
        print('\tPRIZE: ',format(prize,',.2f'),'$',sep='')
        casino_vault-=prize
        print('casino vault: ',format(casino_vault,',.2f'),'$',sep='')
        return prize
    elif dice1==3 and dice2==3:
        print(format('\tHard Six'))
        prize=p2*multiplier
        print('\tPRIZE: ',format(prize,',.2f'),'$',sep='')
        casino_vault-=prize
        print('casino vault: ',format(casino_vault,',.2f'),'$',sep='')
        return prize
    elif dice1+dice2==4:
        print(format('\tEasy Four'))
        prize=p3*multiplier
        print('\tPRIZE: ',format(prize,',.2f'),'$',sep='')
        casino_vault-=prize
        print('casino vault: ',format(casino_vault,',.2f'),'$',sep='')
        return prize
    elif dice1+dice2==6:
        print(format('\tEasy Six'))
        prize=p4*multiplier
        print('\tPRIZE: ',format(prize,',.2f'),'$',sep='')
        casino_vault-=prize
        print('casino vault: ',format(casino_vault,',.2f'),'$',sep='')
        return prize
    else:
        print("")
        print('casino vault: ',format(casino_vault,',.2f'),'$',sep='')
        return 0

# This function is to explain the rules to the user
def instruction_slot(casino_vault):
    print('     This time you are playing against the casino     ')
    print('  The casino have ',format(casino_vault,',.2f'), '$ dollar in its vault',sep='')
    print('  You can win this game by making the casino bankrupt')
    print('           Your balance is 1,000,000.00 $')
    print('                     1$ per roll')
    print('                        PRIZE              ')
    print('          Snake Eyes   1 and 1      ',format(p1,',.2f'),'$',sep='')
    print('          Hard Four    2 and 2      ',format(p2,',.2f'),'$',sep='')
    print('          Hard Six     3 and 3      ',format(p2,',.2f'),'$',sep='')
    print('          Easy Four    4 in total   ',format(p3,',.2f'),'$',sep='')
    print('          Easy Six     6 in total   ',format(p4,',.2f'),'$',sep='')
    print('          ===============================')
    print('                      Good luck!')

#is a positive floating point and no larger than user's balance
def valid2(value,default,money):
    if value=='':
        value=default
        value=str(value)
    while not(value.isdigit()):
        value=input('It must be a number\n')
    value=float(value)
    while not (value<=money) :
        value=float(input('It must be smaller than or equal to your balance:\n'))
        if value=='':
            value=default
    return value
    
