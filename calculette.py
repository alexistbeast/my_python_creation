from tkinter import *
from calculer import *
import ctypes
import math
fenetre = Tk()
fenetre.geometry('800x600')
n = ""
v = ""

# Chargement de l'image pour l'icône
fenetre.title("ma calculatrice")
frame = Frame(fenetre)

# Texte de bienvenue
bienvenue = Label(fenetre, text="Bienvenue sur ma calculatrice", font="Arial 50", bg="gray30", fg="black")

bienvenue.pack(side="top", pady=30)  # Placer le titre en haut avec un espacement vertical
#couleur de fond pour la frame et le fenêtre

fenetre.configure(background="gray30")
frame.configure(background="gray30")
frame.pack(expand=True,padx=18,pady=18)
operateuractuelle = ['+','-','/','*','e']
def RecupValeur(valeur):
    global n
    global v
    v = valeur
    calc = Calcul(valeur,False,None,None) 
    if valeur == "Reset":
        saisie.config(text="")
        Calcul(None,None,None,None)
    else:
        saisie.config(text=saisie.cget("text") + str(valeur))

#chiffres 1 - 9 + parenthèses
Chiffre1 = Button(frame, bg=['gray50'],font="Arial 18",width=10,height=5, text='1',border=5,command=lambda : RecupValeur(1))
Chiffre1.grid(row=1,column=0)
Chiffre2 = Button(frame, bg=['gray50'],font="Arial 18",width=10,height=5, text='2',border=5,command=lambda : RecupValeur(2))
Chiffre2.grid(row=1,column=1)
Chiffre3 = Button(frame, bg=['gray50'],font="Arial 18",width=10,height=5, text='3',border=5,command=lambda : RecupValeur(3))
Chiffre3.grid(row=1,column=2)
Chiffre4 = Button(frame, bg=['gray50'],font="Arial 18",width=10,height=5, text='4',border=5,command=lambda : RecupValeur(4))
Chiffre4.grid(row=2,column=0)
Chiffre5 = Button(frame, bg=['gray50'],font="Arial 18",width=10,height=5, text='5',border=5,command=lambda : RecupValeur(5))
Chiffre5.grid(row=2,column=1)
Chiffre6 = Button(frame, bg=['gray50'],font="Arial 18",width=10,height=5, text='6',border=5,command=lambda : RecupValeur(6))
Chiffre6.grid(row=2,column=2)
Chiffre7 = Button(frame, bg=['gray50'],font="Arial 18",width=10,height=5, text='7',border=5,command=lambda : RecupValeur(7))
Chiffre7.grid(row=3,column=0)
Chiffre8 = Button(frame, bg=['gray50'],font="Arial 18",width=10,height=5, text='8',border=5,command=lambda : RecupValeur(8))
Chiffre8.grid(row=3,column=1)
Chiffre9 = Button(frame, bg=['gray50'],font="Arial 18",width=10,height=5, text='9',border=5,command=lambda : RecupValeur(9))
Chiffre9.grid(row=3,column=2)

parentheseouverte = Button(frame, bg=['gray50'],font="Arial 18",width=10,height=5, text='(',border=5,command=lambda : RecupValeur('('))
parentheseouverte.grid(row=1,column=4)
parentheseferme = Button(frame, bg=['gray50'],font="Arial 18",width=10,height=5, text=')',border=5,command=lambda : RecupValeur(')'))
parentheseferme.grid(row=1,column=5)
point = Button(frame, bg=['gray50'],font="Arial 18",width=10,height=5, text='.',border=5,command=lambda : RecupValeur('.'))
point.grid(row=4,column=4)
# bouton AC reset
Reset = Button(frame, bg=['gray50'],font="Arial 18",width=10,height=5, text='AC',border=5,command=lambda : RecupValeur('Reset'))
Reset.grid(row=3, column=4)

# opération

plus = Button(frame, bg=['gray50'],font="Arial 18",text='+',width=10,height=5, border=5,command=lambda : RecupValeur('+'))
plus.grid(row = 1,column=3)
moins = Button(frame, bg=['gray50'],font="Arial 18",text='-',width=10,height=5, border=5,command=lambda : RecupValeur('-'))
moins.grid(row = 2,column=3)
fois = Button(frame, bg=['gray50'],font="Arial 18",text='*',width=10,height=5, border=5,command=lambda : RecupValeur('*'))
fois.grid(row = 3, column=3)
diviser = Button(frame, bg=['gray50'],font="Arial 18",text='/',width=10,height=5, border=5,command=lambda : RecupValeur('/'))
diviser.grid(row = 4, column=3)
exposant = Button(frame, bg=['gray50'],font="Arial 18",text='^',width=10,height=5, border=5,command=lambda : RecupValeur('^'))
exposant.grid(row=4,column=2)
racinecarre = Button(frame, bg=['gray50'],font="Arial 18",text='√',width=10,height=5, border=5,command=lambda : RecupValeur('√'))
racinecarre.grid(row=4,column=1)
factorielle = Button(frame, bg=['gray50'],font="Arial 18",text='!',width=10,height=5, border=5,command=lambda : RecupValeur('!'))
factorielle.grid(row=2,column=4)
# texte de saisie

saisie = Label(fenetre, bg=['gray50'],font="Arial 18",border=5,width=50,height=5)
saisie.pack(side="bottom",pady=10)

# bouton pour calculer

calculerBTN = Button(frame, bg=['gray50'],font="Arial 18",text="Calculer",width=10,height=5,border=5,command=lambda : Calcul(v,True, saisie.cget('text'),saisie))
calculerBTN.grid(row = 4,column=0)

frame.mainloop()

