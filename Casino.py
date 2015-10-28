__author__ = 'Jure'
import random


x=random.randrange(10)
y=str(x)
guess=raw_input("Vpisi stevilo med 0 in 10:")
if guess==y:
    guessed=True
else:
    guessed=False
poskusov=1
guess
while guessed==False:
    print("Zal " + guess + " ni iskano stevilo")
    guess=raw_input("Poskusite znova. Vpisi stevilo med 0 in 10:")
    poskusov+=1
    if guess==y:
        guessed=True

if poskusov==1:
    print("Vas odgovor je praviln. Za pravilen odgovor ste ptrebovali 1 poskus.")
elif poskusov==2:
    print("Vas odgovor je praviln. Za pravilen odgovor ste ptrebovali 2 poskusa.")
elif poskusov==3 or poskusov==4:
    print("Vas odgovor je praviln. Za pravilen odgovor ste ptrebovali " + poskusov + " poskuse.")
else:
    print("Vas odgovor je praviln. Za pravilen odgovor ste ptrebovali " + poskusov + " poskusov.")