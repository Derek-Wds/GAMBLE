import functions
def main():
    casino_vault=functions.read()
    #a is a sentinel deciding telling the program
    #which case it is
    a=''
    #call the instrucion()
    functions.instruction_slot(casino_vault)
    #let user enter a balance
    money=1000000
    #set default multiplier
    default_multiplier=1
    #let user enter a multiplier
    multiplier=input('Enter your multiplier(DEFAULT 1):\n')
    multiplier=functions.valid2(multiplier,default_multiplier,money)

    #loop
    while not a=='x':
        if casino_vault>0:
            #case1: using the old multiplier and roll again
            if a=='':
                if money>=multiplier:
                    money-=multiplier
                    casino_vault+=multiplier
                    print('==========================')
                    prize=functions.roll2(multiplier,casino_vault)
                    money+=prize
                    casino_vault-=prize
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
                            multiplier=functions.valid2(option,default_multiplier,money)
            #case3: user change a multiplier
            else:
                multiplier=functions.valid2(a,default_multiplier,money)
                money-=multiplier
                casino_vault+=multiplier
                print('==========================')
                prize=functions.roll2(multiplier,casino_vault)
                money+=prize
                casino_vault-=prize
                print('')
                print('Your balance: ',format(money,',.2f'),'$',sep='')
                print('')
                a=input('1)Press ENTER to roll again\n\
2)enter new multiplier\n\
3)enter x to cash your balance\n')
        else:
            a='x'
    functions.ending_chosing(casino_vault,money)
    functions.write(casino_vault)
    functions.score_board(money)


#call the main function
main()
