# Importation de la biblio pour les arbres
from Bib_TDA_PFA import AB, Pile


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


"""
Exo du cours 
"""
def Traiter(A):
    print(A)


# Exo 1

# Preodonne (PERE-FG-FD)
def ParcoursPre(A) :
    if not A.EstVide() :
        Traiter(A.GetRacine())
        ParcoursPre(A.GetSAG())
        ParcoursPre(A.GetSAD())


# Symetrique (FG-PERE-FD)
def ParcoursSym(A) :
    if not A.EstVide() :
        ParcoursSym(A.GetSAG())
        Traiter(A.GetRacine())
        ParcoursSym(A.GetSAD())

        
"""
Resultat 
"""
A = AB('P')
# Ajout fils gauche de A : E
A.AjouterFG('E')

# Ajout fils gauche de E : S 
# A.GetSAG().AjouterFG('S')

# Ajout fils droit de E : A
A.GetSAG().AjouterFD('A')

# Ajout fils gauche de A : M
A.GetSAG().GetSAD().AjouterFG('M')

# Ajout fils droit de P : R
A.AjouterFD('R')

# Ajout fils gauche de R : H
A.GetSAD().AjouterFG('H')

# Ajout fils droit de R : E
A.GetSAD().AjouterFD('E')

# Ajout fils droit de H : O
A.GetSAD().GetSAG().AjouterFD('O')

# Appel Pre : P-E-S-A-M-R-H-O-E 
ParcoursPre(A)
print("########################")
ParcoursSym(A)


# Parcours Symetrique (FG-PERE-FD)
# Resultat : S-E-A-M-P-H-O-R-E


# Parcours Post (FG-FD-PERE)
# Resultat : S-M-A-E-O-H-E-R-P

# Exo 2
"""
Racine : 9, car c est le premier noeud a etre traite lors du parcours Preodonne


"""

# Exo 3
"""
1-
2- 
3- 8 comparaisons
4- 3 comparaisons
5- 3 comparaisons 
"""

# Exo 4
"""
1- (14.5, 1), (14.1, 1), (16.8, 1), (15.3, 1), (18.6, 1), (17.5, 1) === res1 = 6
2- res2 = 
3- L'algo compte le nombre de noeuds plus grands ou egaux a val 
"""

# Exo 5
"""
Produit des valeurs des noeuds d'un arbre binaire
"""
# Traitement multiplication 
def multiplication(val, P):
    if not P.EstVide():
        p = P.Retirer()
        P.Ajouter(p*val)
    else:
        P.Ajouter(val)

        
# Traitement compte branche droit
def CompteDroitPre(A):
    if not A.EstVide() and not A.FD.EstVide():
        print(A.GetRacine())
        return 1 + CompteDroitPre(A.FG) + CompteDroitPre(A.FD)
    else:
        return 0

    
# Preodonne (PERE-FG-FD)
def MultPre(A, P) :
    if not A.EstVide() :
        multiplication(A.GetRacine(), P)
        MultPre(A.GetSAG(), P)
        MultPre(A.GetSAD(), P)
    
        
        
P = Pile()

MultPre(AB(), P)

if not P.EstVide() : print(P.Premier())

print("###########Compte Droit ##############")

print(CompteDroitPre(A))



# Exo 6
# Fonction compte feuille
# A1 
A1 = AB(12)

A1.AjouterFD(15)
A1.AjouterFG(8)

A1.GetSAG().AjouterFG(4)
A1.GetSAG().GetSAG().AjouterFD(7)



# Retourne 1 si c est un noeud
def CompteNoeud(A):
    if A.FD.EstVide() and A.FG.EstVide():
        print(A.GetRacine())
        return 1
    else:
        return 0

# Retourne la valeur du noeud 
def ValeurNoeud(A):
    if A.FD.EstVide() and A.FG.EstVide():
        return A.GetRacine()
    else:
        return 0

    
# Compte les feuille 
def CompteFeuillePre(A):
    if not A.EstVide() :
        n = CompteNoeud(A)
        n1 = CompteFeuillePre(A.FG)
        n2  = CompteFeuillePre(A.FD)
        return n + n1 + n2
    else:
        return 0


# Somme des feuille 
def SommeFeuillePre(A):
    if not A.EstVide() :
        n = ValeurNoeud(A)
        n1 = SommeFeuillePre(A.FG)
        n2  = SommeFeuillePre(A.FD)
        return n + n1 + n2
    else:
        return 0

    
print("###########Compte Feuille ##############")

print(CompteFeuillePre(A1))


print("###########Somme Feuille ##############")

print(SommeFeuillePre(A1))
