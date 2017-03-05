def read():
    k=open('/Users/lihongyi/Desktop/Vault.txt')
    casino_vault=float(k.read())
    k.close()
    return casino_vault

#This function is to make sure that the bet input is valid
def valid1(value,default,money):
    if value=='':
        value=default
    value=float(value)
    while not (value>=0 and value<=money) :
        value=input('It must be \n\
        1）larger than or equal to 0 \n\
        2) smaller than or equal to your balance:\n')
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
def roll(casino_vault,money,bet1,bet2,bet3,tbet):
    print('Roll')
    import random # import thre random function
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
        casino_vault-=bet3*31
        money+=bet3*31
        prize=bet3*31
    elif (total>=4 and total<=10):
        print('small win')
        casino_vault-=bet2*2
        money+=bet2*2
        prize=bet2*2
    elif (total>=11 and total<=17):
        print('big win')
        casino_vault-=bet1*2
        money+=bet1*2
        prize=bet1*2
    net=prize-tbet
    print('')
    print('The net win for this bet is \n',format(net,',.2f'),'$',sep='')
    return money, casino_vault


# This function is to explain the rules to the user
def instruction(casino_vault):
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
    print('Big\t\tsum: 11 to 17(except for triple)\t\t1 to 1')
    print('Small\t\tsum: 4 to 10(except for triple)\t\t\t1 to 1')
    print('Triple\t\tthree dices have the same value\t\t\t30 to 1')



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
        print('At least you got you buffet ticket!')
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
    
    

casino_vault=read()
#a is a sentinel deciding telling the program
#which case it is
a=''
#call the instrucion()
instruction(casino_vault)
#let user enter a balance
money=1000000
tbet=0
#loop
bet1,bet2,bet3,tbet = bet(money,tbet)
while not a=='x':
    if casino_vault>0:
        #case1: using the old bet and roll again
        if a==''and tbet<=money:
            casino_vault+=tbet
            money-=tbet
            show_bet(bet1,bet2,bet3)
            money,casino_vault=roll(casino_vault,money,bet1,bet2,bet3,tbet)
            print('='*70)
            print('')
            print('Your balance: ',format(money,',.2f'),'$',sep='')
            print('casino vault: ',format(casino_vault,',.2f'),'$',sep='')
            print('')
            #different value of a can allow user
            #to roll again with the same bet;
            #change the bet and roll again;
            #or exit the game
            a=input('1)Press ENTER to roll again with the same bet\n\
2)enter a for a different bet\n\
3)enter x to cash your balance\n')
        elif money==0:
            a='x'
        #case2: user change a bet
        else:
            bet1,bet2,bet3,tbet=bet(money,tbet)
            casino_vault+=tbet
            money-=tbet
            show_bet(bet1,bet2,bet3)
            money,casino_vault=roll(casino_vault,money,bet1,bet2,bet3,tbet)
            print('='*70)
            print('')
            print('Your balance: ',format(money,',.2f'),'$',sep='')
            print('casino vault: ',format(casino_vault,',.2f'),'$',sep='')
            print('')
            a=input('1)Press ENTER to roll again with the same bet\n\
2)Press a for a different bet\n\
3)enter x to cash your balance\n')
    else:
        a='x'
ending_chosing(casino_vault,money)
write(casino_vault)
score_board(money)



#call the main function
#How to prevent bad input like letters?
#improve the prize mechanism
