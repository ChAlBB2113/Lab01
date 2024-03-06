def main():
    class Domanda:
        def __init__ (self,numero,ask,difficulty,rispostaEsatta,rispostaErrata1,rispostaErrata2,rispostaErrata3):
            self.numero=numero
            self.ask=ask
            self.difficulty=difficulty
            self.rispostaEsatta=rispostaEsatta
            self.rispostaErrata1=rispostaErrata1
            self.rispostaErrata2 = rispostaErrata2
            self.rispostaErrata2 = rispostaErrata3

    listaDomande = []
    numeroDomande = 1

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
            domanda=Domanda(numeroDomande,ask, difficulty, rispostaEsatta, rispostaErrata1, rispostaErrata2, rispostaErrata3)
            listaDomande.append(domanda)
            numeroDomande = numeroDomande + 1

        file.close()
    except FileNotFoundError:
        print("file non trovato")

    nuneroDomande=numeroDomande-1

    print(listaDomande[28].numero)




main()