rate=30
r=30
exp_p=0
exp_b=0
print('rounds\tp(round)\tp(banker win)\tbanker earn if win\tplayer earn if win\texpectation(player)\texpectation(banker)')
for i in range(1,r+1,1):
    p=(35/36)**(i-1)
    win=(35/36)*p
    end=p*(1/36)
    profit_b=i
    profit_p=rate-(i-1)
    exp_p+=(end*profit_p)
    exp_b-=(end*profit_p)
    ecp=exp_p-win*i
    ecb=exp_b+win*i
    for k in range(1,r+1,1):
        if i==k:
            print(format(i,'^5'),'\t',format(p,'^8.2f'),'\t',format(win,'^8.2f'),'\t',format(profit_b,'^18.3f'),' \t',format(profit_p,'^18.3f'),'\t',format(ecp,'^19.2f'),'\t',format(ecb,'^19.2f'))

