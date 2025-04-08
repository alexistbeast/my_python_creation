import math
class Calcul:
    def __init__(self, numero, activer,calculfini,saisie):
        self.numero = numero
        self.activer = activer
        self.calculfini = calculfini
        self.saisie = saisie
        if activer:
            self.calculer()
    def calculer(self):
        if "!" in self.calculfini:
            self.calculfini = self.calculfini.replace("!", "math.factorial(") + ")"
        elif "√" in self.calculfini:
            self.calculfini = self.calculfini.replace("√","math.sqrt(") + ")"
        if "^" in self.calculfini:
            self.calculfini = self.calculfini.replace("^","**")
        resultat = eval(self.calculfini)
        if ValueError:
            self.saisie.config(text="")
            self.saisie.config(text="le calcul que vous essayer de faire est impossible ou trop grand")
        self.saisie.config(text=str(resultat))



