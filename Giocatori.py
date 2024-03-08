class Giocatori:
    def __init__(self, nickname, punteggio):
        self.nickname= nickname
        self.punteggio= punteggio

    def __lt__(self, other):
        #if self.punteggio == other.punteggio:
        #    return - self.nickname < other.nickname
        #else:
        return  self.punteggio < other.punteggio
