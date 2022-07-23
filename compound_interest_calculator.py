import time
i0=1000 #investimento iniziale
percent=0.025 #percentuale di guadagno giornaliera
imensile=i0 #*percent+i0
giorno=1
print('''
calcolo dei profitti nel tempo con interesse composto
- capitale iniziale
- numero di unita di tempo
- guadagno percentuale per unita di tempo

	''')
def profitto():
    # x e'investimento iniziale
    # percent e' la percentuale media di guadagno giornaliero
    # giorni sono i giorni dell' investimento
    capitale=int(input('initial capital ($)                      -> \t'))
    giorni=int(input("units of time (n)                        -> \t"))
    percent=float(input("gain for unit of time (%)                -> \t"))

    giorno=1
    capitaleiniziale=capitale
    percent=percent/100 #inserisco cosi' la percentuale espressa in %
    print('_'*30)
    visual=input("visualize full results?    ( y / n ) ")
    if str(visual)=='y' or str(visual)=='Y':
        print(" asset	       unit ")
    else:
        pass
    while giorno<giorni:
        capitale+= capitale*percent
        giorno+=1
        if visual=='y' or visual=='Y':
            print('\t',int(capitale) ,"\t\t\t\t", giorno)

    print('\ncapitale lordo di             -> \t' + str(int(round(capitale)))+" $")
    print('profitto percentuale del -> \t\t' + str(int(round(capitale/capitaleiniziale*100-100,2))) +' %')
    print("profitto netto del           -> \t" + str(int(round(capitale-capitaleiniziale,0))) +" $")
    time.sleep(1)

while True:
    profitto()
    esci=input('continue? y  /  n   ')
    print('_'*60)
    if esci=='n':
        break
