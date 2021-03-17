import time
i0=1000 #investimento iniziale
percent=0.025 #percentuale di guadagno giornaliera
imensile=i0 #*percent+i0
giorno=1
print('''
	
	Programma che calcola i profitti con la percentuale attesa di profitto nel tempo

	''')
def profitto():
    # x e'investimento iniziale
    # percent e' la percentuale media di guadagno giornaliero
    # giorni sono i giorni dell' investimento
    capitale=int(input('inserisci il capitale iniziale '))
    percent=float(input("la percentuale ex(8, per un 8% ) di guadagno per ogni unita' di tempo "))
    giorni=int(input("numero di unita' di tempo "))
    giorno=1
    capitaleiniziale=capitale
    percent=percent/100 #inserisco cosi' la percentuale espressa in %
    print('_'*30)
    visual=input("vuoi visualizzare unita' per unita' ? y/n ")
    if str(visual)=='y' or str(visual)=='Y':
        print(" capitale  |      unita'  |")
    else:
        pass
    while giorno<giorni:
        capitale+= capitale*percent
        giorno+=1
        if visual=='y' or visual=='Y':
            print(int(capitale) ,' | ', giorno)

    print('_'*30)
    print('capitale lordo di  ' + str(int(round(capitale))))
    print('profitto percentuale del ' + str(int(round(capitale/capitaleiniziale*100-100,2))) +' %')
    print("profitto netto del  " + str(int(round(capitale-capitaleiniziale,0))) +" euro")
    time.sleep(1)

while True:
    profitto()
    esci=input('continue? y  /  n   ')
    print('_'*60)
    if esci=='n':
        break
