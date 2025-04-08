from tkinter import *
from PIL import Image, ImageTk  # Pillow pour redimensionner l'image
import random
from tkinter import simpledialog
# Fenêtre principale
fenetre = Tk()
fenetre.geometry("1920x1080")  # Définissez la taille de la fenêtre

# Charger et redimensionner l'image
original_image = Image.open("images/blackjack.png")
resized_image = original_image.resize((1920, 1080), Image.Resampling.LANCZOS)  # Adapter à la taille de la fenêtre
background_image = ImageTk.PhotoImage(resized_image)

# Afficher l'image en arrière-plan
background_label = Label(fenetre, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# listes

cartes = {"K":10,"Q":10,"J":10,"10":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2,"A":1}

#boutons et labels

piocher_joueur = Button(fenetre,width=10,height=5,text="piocher",font="Calibri 18",bg="grey")
piocher_joueur.pack(side=BOTTOM,anchor="w")

piocher_joueur.config(command=lambda b = piocher_joueur : piocher("pioche_joueur"))


points_joueur = Label(fenetre,font="Calibri 18")
points_joueur.pack(side=BOTTOM,anchor=CENTER)

points_ordinateur = Label(fenetre,font="Calibri 18")
points_ordinateur.pack(side=TOP,anchor=CENTER)

carte_piocher_joueur = Label(fenetre,width=10,height=5,font="Calibri 18")
carte_piocher_joueur.pack(side=BOTTOM,anchor="n")

stand_joueur = Button(fenetre,width=10,height=5,text="Stand",font="Calibri 18",bg="grey")
stand_joueur.pack(side=BOTTOM)

stand_joueur.config(command=lambda : ordinateur())


message_gagne = Label(fenetre, font="Calibri 30")


carte_piocher_ordinateur = Label(fenetre,width=10,height=5,font="Calibri 18")
carte_piocher_ordinateur.pack(side=TOP,anchor="s")

valeur_joueur_liste = []
valeur_ordinateur_liste = []
#piocher
valeur_ordinateur_additionnee = 0
def piocher(b):
    global valeur_ordinateur_additionnee
    global valeur_joueur_additionnee
    if b == "pioche_joueur":
        carte_joueur, valeur_joueur = random.choice(list(cartes.items()))
        valeur_joueur_liste.append(valeur_joueur)
        valeur_joueur_additionnee = sum(valeur_joueur_liste)
        points_joueur.config(text=valeur_joueur_additionnee)
        carte_piocher_joueur.config(text=carte_joueur)
    if b == "pioche_ordinateur":
        carte_ordinateur, valeur_ordinateur = random.choice(list(cartes.items()))
        valeur_ordinateur_liste.append(valeur_ordinateur)
        valeur_ordinateur_additionnee = sum(valeur_ordinateur_liste)
        points_ordinateur.config(text=valeur_ordinateur_additionnee)
        carte_piocher_ordinateur.config(text=carte_ordinateur)
        points_ordinateur.config(text=valeur_ordinateur_additionnee)
        verifier_resultat()
def verifier_resultat():
    global valeur_ordinateur_additionnee

    # L'ordinateur continue à piocher tant qu'il a moins de 17 points
    if valeur_ordinateur_additionnee < 17:
        fenetre.after(1000, lambda: piocher("pioche_ordinateur"))  # Attendre 1 seconde avant de piocher une nouvelle carte
    else:
        # Une fois que l'ordinateur a 17 ou plus, déterminer le gagnant
        verifier_gagnant()

# Vérifier qui a gagné
def verifier_gagnant():
    global valeur_ordinateur_additionnee, valeur_joueur_additionnee
    
    if valeur_ordinateur_additionnee > 21:
        message_gagne.config(text="Vous avez gagné!")
        message_gagne.pack(anchor=CENTER)
        reset()
    elif valeur_joueur_additionnee > 21:
        message_gagne.config(text="L'ordinateur a gagné!")
        message_gagne.pack(anchor=CENTER)
        reset()
    elif valeur_ordinateur_additionnee == valeur_joueur_additionnee:
        message_gagne.config(text="Égalité!")
        message_gagne.pack(anchor=CENTER)
        reset()
    elif valeur_ordinateur_additionnee > valeur_joueur_additionnee:
        message_gagne.config(text="L'ordinateur a gagné!")
        message_gagne.pack(anchor=CENTER)
        reset()
    elif valeur_joueur_additionnee > valeur_ordinateur_additionnee:
        message_gagne.config(text="Vous avez gagné!")
        message_gagne.pack(anchor=CENTER)
        reset()
    elif valeur_joueur_additionnee > 21:
        message_gagne.config(text="Vous avez perdu")
        message_gagne.pack(anchor=CENTER)
        reset()
def ordinateur():

    fenetre.after(1000, lambda : piocher("pioche_ordinateur"))
def reset():
    global valeur_joueur_additionnee
    global valeur_ordinateur_additionnee
    recommencer = simpledialog.askstring(title="recommencer",prompt="voulez vous recommencer : Oui / Non")
    if recommencer == 'Oui':
        valeur_joueur_liste.clear()
        valeur_ordinateur_liste.clear()
        valeur_joueur_additionnee = 0
        valeur_ordinateur_additionnee = 0
        points_joueur.config(text="")
        points_ordinateur.config(text="")
        carte_piocher_joueur.config(text="")
        carte_piocher_ordinateur.config(text="")
        message_gagne.pack_forget()
    else:
        fenetre.quit()
#loop

fenetre.mainloop()