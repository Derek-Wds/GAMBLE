import functions
casino_vault=functions.read()
#a is a sentinel deciding telling the program
#which case it is
a=''
#call the instrucion()
functions.instruction_sic_bo(casino_vault)
#let user enter a balance
money=1000000
tbet=0
#loop
bet1,bet2,bet3,tbet = functions.bet(money,tbet)
while not a=='x':
    if casino_vault>0:
        #case1: using the old bet and roll again
        if a==''and tbet<=money:
            casino_vault+=tbet
            money-=tbet
            functions.show_bet(bet1,bet2,bet3)
            money,casino_vault=functions.roll1(casino_vault,money,bet1,bet2,bet3,tbet)
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
            bet1,bet2,bet3,tbet=functions.bet(money,tbet)
            casino_vault+=tbet
            money-=tbet
            functions.show_bet(bet1,bet2,bet3)
            money,casino_vault=functions.roll1(casino_vault,money,bet1,bet2,bet3,tbet)
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
functions.ending_chosing(casino_vault,money)
functions.write(casino_vault)
functions.score_board(money)



#call the main function
#How to prevent bad input like letters?
#improve the prize mechanism
