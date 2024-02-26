import os
import datetime

naziv=''
ulica= ''
pt_sjedista=''
grad_sjedišta=''
OIB=''
stanje_racuna=''
valuta=''
broj_racuna=''
promet=[stanje_racuna]

def ocisti_ekran():
    os.system('cls' if os.name=='nt' else 'clear')
    
def generiranje_br_rn():#BA-GODINA-MJESEC-Redni_broj
    global broj_racuna
    broj=''
    godina=str(datetime.date.today().year)
    mjesec= str(datetime.date.today().month)
    broj = broj.zfill(5)
    broj_racuna = 'BA' + '-' + godina + '-' + mjesec + '-' + broj
    print(broj_racuna)
    return (broj_racuna)


    
def stanje_rn():
    global naziv, ulica, pt_sjedista, grad_sjedišta, OIB, stanje_racuna, valuta, broj_racuna
    print(f'''
            +++++++++++++++++++PY BANK+++++++++++++++++++++
                      Dobrodošli u PY Bank
            Ime tvrtke:     {naziv}
            Adresa:         {ulica}, {pt_sjedista}, {grad_sjedišta}, 
            OIB tvrtke:     {OIB}
            Broj računa:    {broj_racuna}
            
            Stanje računa:  {stanje_racuna}{valuta}''')

def kreiranje_racuna_tvrtke():
    global naziv, ulica, pt_sjedista, grad_sjedišta, OIB, stanje_racuna, valuta, broj_racuna
    naziv=input('Unesite naziv tvrtke: ')
    ulica= input('Unesite ulicu i broj sjedišta: ')
    pt_sjedista=input('Unesite poštanski broj sjedišta: ')
    grad_sjedišta=input('Unesite grad sjedišta: ')
    OIB= input ('Unesite OIB tvrtke: ')
    if len(OIB) == 11:
        print('Unijeli ste OIB s dovoljnim brojem znakova.')
    else:
        print('OIB mora imati točno 11 znakova, pokušajte ponovno. ')
        return
    broj_racuna= generiranje_br_rn() 
    valuta=input('Odaberite valutu KN ili EUR.').upper()
    stanje_racuna=float(input('Položite željeni iznos: '))
    stanje_rn()
    return
    
 
def glavni_izbornik():
    g_izbornik='''
    Odaberite:
    1 .Kreiranje računa
    2. Prikaz stanja
    3. Prikaz prometa
    4. Polog
    5. Podizanje novaca
    6. Izlaz '''
    print(g_izbornik)
    
def polog():
    global stanje_racuna
    polog=float(input('Unesite iznos koji želite položiti: '))
    promet.append(polog)
    stanje_racuna += polog
    print(f'Novo stanje računa je {stanje_racuna} {valuta}')
    return

def podizanje_iznosa():
    global stanje_racuna
    
    iznos=float(input('Unesite iznos koji želite podići: '))
    if iznos <= stanje_racuna:
        promet.append(iznos)
        stanje_racuna -=iznos
        print(f'Novo stanje računa je {stanje_racuna} {valuta}')
        return
    else:
        print('Nedovoljan iznos na računu. ')

       
def promet_rn():
    for i in promet:
        print(i, end = '\n')
    
def main():
              
    while True:
            glavni_izbornik()
            izbor=input("Odaberite opciju: ")
            if izbor=='1':
                ocisti_ekran()
                kreiranje_racuna_tvrtke()
            elif izbor=='2':
                ocisti_ekran()
                stanje_rn()
            elif izbor=='3':
                ocisti_ekran()
                promet_rn() 
            elif izbor=='4':
                ocisti_ekran()
                polog()
            elif izbor=='5':
                ocisti_ekran()
                podizanje_iznosa()
            elif izbor=='6':
                break
            else:
                ocisti_ekran()
                print("Pogresan izbor")
                print()
                input('za nastavak stisni enter')
            

main() 