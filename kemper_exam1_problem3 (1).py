import random
import pylab as py


def Martingale():
    Monies=20
    Bet = 1
    while 0< Monies <40:
        x=random.randint(-1,36)
        if x<2:
            Monies=Monies-Bet
            Bet=2*Bet
            if (Monies-Bet)<=0:
                Bet=Monies
            print Monies
            
        elif x%2==0:
            Monies=Monies+Bet
            Bet=1
            print Monies
            
        else:
            Monies=Monies-Bet
            Bet=2*Bet
            if (Monies-Bet)<=0:
                Bet=Monies
            print Monies
    if Monies==40:
        print "Winner"
    elif Monies==0:
        print "Loser"
    print
    return Monies
            
runs=1
while runs<=8000:
    A=Martingale()
    py.plot(runs,A,"r.")
    runs=runs+1
      
py.title("Martingale")
py.xlabel("x", fontsize=16)
py.ylabel("y", fontsize=16)
py.show()
py.savefig("Graphhw.pdf")