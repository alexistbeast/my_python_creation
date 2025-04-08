import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

# Création de la fenêtre principale
f = ttk.Window(themename="cyborg")  # Thème bootstrap (ex: flatly, darkly, superhero, cyborg)
f.title("To-Do List Moderne ✅")
f.geometry("500x600")

# Liste pour stocker les tâches (Labels & Checkbuttons)
tasks = []

# Fonction pour ajouter une tâche
def ajouter_tache():
    tache = entry_ajouter.get().strip()
    if tache:
        # Créer un cadre pour la tâche
        frame = ttk.Frame(task_frame)
        frame.pack(fill="x", pady=5, padx=10)

        # Label de la tâche
        label = ttk.Label(frame, text=tache, font=("Calibri", 14), bootstyle=INFO)
        label.pack(side="left", padx=10)
        
        # Case à cocher
        check_var = ttk.IntVar()
        checkbutton = ttk.Checkbutton(frame, variable=check_var, bootstyle="success-round-toggle")
        checkbutton.pack(side="right")

        # Modifier la tâche au clic
        label.bind("<Button-1>", lambda e, lbl=label: modifier_tache(lbl))

        # Ajouter à la liste
        tasks.append((label, checkbutton, frame))

        # Effacer l'Entry après ajout
        entry_ajouter.delete(0, ttk.END)
    else:
        messagebox.showwarning("Attention", "La tâche ne peut pas être vide !")

# Fonction pour modifier une tâche
def modifier_tache(label):
    new_text = entry_ajouter.get().strip()
    if new_text:
        label.config(text=new_text)
        entry_ajouter.delete(0, ttk.END)
    else:
        messagebox.showwarning("Attention", "Entrez une nouvelle tâche !")

# Fonction pour supprimer toutes les tâches cochées
def supprimer_taches():
    global tasks
    tasks = [t for t in tasks if not t[1].variable.get()]
    for label, checkbutton, frame in tasks:
        frame.pack_forget()
    tasks = [t for t in tasks if t[2].winfo_ismapped()]

# Zone de saisie pour ajouter une tâche
entry_ajouter = ttk.Entry(f, width=40, bootstyle="info")
entry_ajouter.pack(pady=10, padx=20)

# Bouton pour ajouter une tâche
bouton_ajouter = ttk.Button(f, text="Ajouter Tâche", command=ajouter_tache, bootstyle=PRIMARY)
bouton_ajouter.pack(pady=5)

# Cadre pour afficher les tâches
task_frame = ttk.Frame(f, bootstyle="light")
task_frame.pack(fill="both", expand=True, pady=10, padx=10)

# Bouton pour supprimer les tâches terminées
bouton_supprimer = ttk.Button(f, text="Supprimer tâches terminées", command=supprimer_taches, bootstyle=DANGER)
bouton_supprimer.pack(pady=10)

# Lancer l'application
f.mainloop()
