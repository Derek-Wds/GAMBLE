import random
def roll(i,money,bet):
    dice1=int(random.randint(1,6))# To give each dice
    dice2=int(random.randint(1,6))# a random value
    dice3=int(random.randint(1,6))
    if (dice1==dice2 and dice1==dice3):
        money+=bet*odds
        i=30
    return money, i

r=int(input('How many times do you want to test?\n'))
odds=int(input('What is the odds?\n'))
ak=0
bk=0
ck=0
dk=0
ek=0
fk=0
negative=0
zero=0


for k in range(1,r+1):
    i=0
    money=odds
    while i<odds:
        money-=1
        money,i=roll(i,money,1)
        i+=1
    if money-odds<0:
        negative+=1
    elif money-odds==0:
        zero+=1
    elif money-odds>0 and money-odds<5:
        ak+=1
    elif money-odds>=5 and money-odds<10:
        bk+=1
    elif money-odds>=10 and money-odds<15:
        ck+=1
    elif money-odds>=15 and money-odds<20:
        dk+=1
    elif money-odds>=20 and money-odds<25:
        ek+=1
    elif money-odds>=25:
        fk+=1
positive=r-negative-zero
print('total\tnegative\tpositive\t0\t0 to 5\t5 to 10\t10 to 15\t15 to 20\t20 to 25\t25 to 30')
print(r,'\t',negative,'\t',positive,'\t',zero,'\t',ak,'\t',bk,'\t',ck,'\t',dk,'\t',ek,'\t',fk)
print('The posibility of making money is','\t',positive/r)
print('The posibility of a draw is','\t',zero/r)
