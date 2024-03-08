import Domanda #se definisco una classe fuori dal main, per lavorare poi nel main
#con suoi oggetti e metodi devo importare la classe nel file del main fuori dal main
#e poi prima di usare un suo metodo nel main devo usare notazione puntata per indicare la classe di cui
#è quel metodo
import Giocatori

import random

def main(): #dopo il main devo indentare



#classe Domanda

#    class Domanda:
#        def __init__ (self,numero,ask,difficulty,rispostaEsatta,rispostaErrata1,rispostaErrata2,rispostaErrata3):
#           self.numero=numero
#            self.ask=ask
#            self.difficulty=difficulty
#            self.rispostaEsatta=rispostaEsatta
#            self.rispostaErrata1=rispostaErrata1
#            self.rispostaErrata2 = rispostaErrata2
#            self.rispostaErrata2 = rispostaErrata3



    #main vero e proprio


    #inizializzo lista e vuota e contatore (per sapere quante domande ci sono,
    # e cosi per ogni domanda che salvo le assegno il numero della posiozione nel file
    #come attributo "numero" che ho definito nel costruttore che magari torna utile
    listaDomande = []
    numeroDomande = 1

    #leggo domande.txt e lo salvo in una lista di oggetti "domanda" di classe Domanda
    try:
        file=open("domande.txt","r")
        a = True
        while a:
            line = file.readline().strip()
            if line == "":
                a = False
                continue
            ask = line
            line = file.readline().strip()
            difficulty = int(line)
            line = file.readline().strip()
            rispostaEsatta= line
            line = file.readline().strip()
            rispostaErrata1 = line
            line = file.readline().strip()
            rispostaErrata2 = line
            line = file.readline().strip()
            rispostaErrata3 = line
            file.readline()
            domandaTemp=Domanda.Domanda(numeroDomande,ask, difficulty, rispostaEsatta, rispostaErrata1, rispostaErrata2, rispostaErrata3)
            listaDomande.append(domandaTemp)
            numeroDomande = numeroDomande + 1

        file.close()
    except FileNotFoundError:
        print("file delle domande non trovato")


    livelloMax=0
    for i in listaDomande:
        if i.difficulty > livelloMax:
            livelloMax=i.difficulty

    punteggio=0
    #ora ho una lista di oggetti domanda; devo impostare il gioco
    livelloCorrente=0
    procedi=True;
    while livelloCorrente<=livelloMax and procedi==True:
        listaDomandeCorrenti=[]
        listaIndici=[]
        indice=0
        for i in listaDomande:
            if i.difficulty == livelloCorrente:
                listaDomandeCorrenti.append(i)
                listaIndici.append(indice)
                indice=indice+1
        n=random.choice(listaIndici)
        random.shuffle(listaDomandeCorrenti)
        domandaPosta= listaDomandeCorrenti[n]
        listaRisposte=[domandaPosta.rispostaEsatta, domandaPosta.rispostaErrata1, domandaPosta.rispostaErrata2, domandaPosta.rispostaErrata3]

        random.shuffle(listaRisposte)#shuffle non ritorna nulla occhio! Cambia ordine della sequenza e basta3

        print(f"livello {livelloCorrente}) {domandaPosta.ask}")
        print(f"1. {listaRisposte[0]}")
        print(f"2. {listaRisposte[1]}")
        print(f"3. {listaRisposte[2]}")
        print(f"4. {listaRisposte[3]}")
        rispostaData= int(input("Inserisci la risposta: "))
        if listaRisposte[rispostaData-1]==domandaPosta.rispostaEsatta:
            print("Risposta corretta!")
            livelloCorrente=livelloCorrente+1
            punteggio=punteggio+1
        else:
            print(f"Risposta sbagliata! La risposta corretta era: {listaRisposte.index(domandaPosta.rispostaEsatta)+1} ")
            procedi=False

    print(f"Hai totalizzato {punteggio} punti")
    nome=input("Inserisci il tuo nickname: ")
    giocatore=Giocatori.Giocatori(nome,punteggio)

    listaGiocatori=[]
    try:
        filePunti= open("punti.txt", "r")
        for i in filePunti:
            lineCampi=i.strip().split()
            nickname= lineCampi[0]
            punteggio=int(lineCampi[1])
            giocatoreTemp=Giocatori.Giocatori(nickname, punteggio)
            listaGiocatori.append(giocatoreTemp)
        filePunti.close()
    except FileNotFoundError:
        print("file dei punti non trovato")

    listaGiocatori.append(giocatore)

    listaGiocatori.sort(reverse=True)


    try:
        filePunti= open("punti.txt", "w")
        for i in listaGiocatori:
            print(f"{i.nickname} {i.punteggio}",file=filePunti)
        filePunti.close()
    except FileNotFoundError:
        print("file dei punti non trovato")











main()