# Importation de la biblio pour les arbres
from Bib_TDA_PFA import AB


# Creation d'un arbre vide
A1 = AB()


# Verification arbre vide
def verificationArbre(AB):
    if AB.EstVide():
        print("A1  vide")
    else:
        print("A1 pas vide")


# Ajout du noeud racine:12
A1.SetRacine(12)
verificationArbre(A1)

# Ajout fils gauche
A1.FG.SetRacine(6)

# Ajouter fils droit
A1.FD.SetRacine(15)

# Arbre B1 ayant un fils gauche 6 et un fils droit 15
B1 = AB(12)
B1.AjouterFG(6)
B1.AjouterFD(15)


print("Racine A1", A1.GetRacine())
print("Fils gauche racine", A1.GetSAG().GetRacine())
print("Fils droit racine", A1.GetSAD().GetRacine())

print("Racine B1", B1.GetRacine())
print("Fils gauche racine", B1.GetSAG().GetRacine())
print("Fils droit racine", B1.GetSAD().GetRacine())
