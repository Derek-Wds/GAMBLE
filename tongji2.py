import random
def roll(money,bet):
    dice1=int(random.randint(1,6))# To give each dice
    dice2=int(random.randint(1,6))# a random value
    dice3=int(random.randint(1,6))
    if (dice1==dice2 and dice1==dice3):
        money+=bet*(odds)
    return money

r=int(input('How many times do you want to test?\n'))
odds=int(input('What is the odds?\n'))
k=int(input('How many money do you have?\n'))
ak=0
bk=0
ck=0
dk=0
ek=0
fk=0
gk=0
negative=0
zero=0

for u in range(1,r+1):
    i=0
    money=k
    while i<k:
        money-=1
        money=roll(money,1)
        i+=1
    if money-k<0:
        negative+=1
    elif money-k==0:
        zero+=1
    elif money-k>0 and money-k<31:
        ak+=1
    elif money-k>=31 and money-k<61:
        bk+=1
    elif money-k>=61 and money-k<91:
        ck+=1
    elif money-k>=91 and money-k<121:
        dk+=1
    elif money-k>=121 and money-k<151:
        ek+=1
    elif money-k>=151 and money-k<181:
        fk+=1
    elif money-k>=181:
        gk+=1
positive=r-negative-zero

print('total\tnegative\tpositive\t0\t0 to 31\t31 to 61\t61 to 91\t91 to 121\t121 to 151\t151 to 181\t>181')
print(r,'\t',negative,'\t',positive,'\t',zero,'\t',ak,'\t',bk,'\t',ck,'\t',dk,'\t',ek,'\t',fk,'\t',gk)
print('The posibility of making money is','\t',positive/r)
print('The posibility of not losing money is','\t',(positive+zero)/r)
