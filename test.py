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
                                 P
                              /      \
                             E        R
                          /    \    /   \
                         S      A   H   E
                               /     \ 
                              M       O
Preodonne : 
P-E-S-A-M-R-H-O-E

Symetrique:
S-E-M-A-P-H-O-R-E

"""
# Construction de l arbre

A = AB('P')
# Ajout fils gauche de A : E
A.AjouterFG('E')

# Ajout fils gauche de E : S 
A.GetSAG().AjouterFG('S')

# Ajout fils droit de E : A
A.GetSAG().AjouterFD('A')

# Ajout fils gauche de A : M
A.GetSAG().GetSAD().AjouterFG('M')

# Ajout fils droit de P : R
A.AjouterFD('R')

# Ajout fils gauche de R : H
# A.GetSAD().AjouterFG('H')

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
ParcoursPre A0: 

9 – 5 – 3 – 1 – 4 – 8 – 7 – 15 – 12 – 14 – 25 – 29 –  27

1- Parcours symetrique (FG-PERE-FD) :
1-3-4-5-7-8-9-12-14-15-25-27-29

1-3-4-5-7-8-9-12-14-15-25-27-29


2- Racine : 9, car c est le premier noeud a etre traite lors du parcours Preodonne

3- 
                                 9
                              /    \
                           5         15
                         /   \      /   \
                       3      8   12     25
                      / \    /     \       \
                    1    4  7       14      29
                                           /
                                           27

"""

# Exo 3
"""
Liste: 25, 15, 33, 20, 18, 7, 41, 28, 30

                              25
                           /     \ 
                          15      33
                         /  \    /   \
                        7   20  28    41
                           /     \
                          18      30
                    


1-                               25
                               /    \
                              15     33
                             /  \   /  \
                            7   20 28   41
                               /        /
                              18       30
  
2-
Nouvelle liste : 25, 33, 30, 18, 7, 15,
20, 41, 28



                                  25
                               /     \
                              18      33
                            /    \   /  \ 
                           7     20 30   41
                            \       /
                            15     28 
 
3-     25, 15, 33, 20, 18, 7, 41, 28, 30 

       8 comparaisons



4-   
      7, 15, 18, 20, 25, 28, 30, 33, 41
 
      Recherche: 28
      7, 15, 18, 20  -25-     28, 30, 33, 41
      28 ? 25

      28, 30, 33, 41
      
      Recherche: 28
      28 -30- 33, 41
      28 ? 30

      
      28
     
      Recherche: 28
      28
      28 == 28

      3 comparaisons

5- 3 comparaisons 
"""

# Exo 4
"""

1- Exam(T, 14) 
             (14.5, 1), (14.1, 1), (16.8, 1), (15.3, 1), (18.6, 1), (17.5, 1) === res1 = (1+1+1+1+1+1)= 6


2- Exam(T, 10)
   
res2 = 


3- L'algo compte le nombre de noeuds plus grands ou egaux a val 
"""

# Exo 5
"""
Produit des valeurs des noeuds d'un arbre binaire
"""
def multiplication(val, P):
    """
    Traitement multiplication
    Qui consiste a empiler le produit des noeuds

    2*5*3*9
    2

    2*5=10

    10*3= 30
    
    30*9= 180

    """
    if not P.EstVide():
        p = P.Retirer()
        P.Ajouter(p*val)
    else:
        P.Ajouter(val)

        
def CompteDroitPre(A):
    """
    Traitement compte branche droit de l arbre
    """
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
    
        
"""
A1
                        12
                       /  \
                      6    15
                         

"""        
        
P = Pile()

print("########### Produit des valeur de noeuds ##############")

MultPre(A1, P)


if not P.EstVide() : print("produit des noeuds :", P.Premier())

print("###########Compte Droit ##############")

print(CompteDroitPre(A))



# Exo 6
# Fonction compte feuille
# A1

"""
    A1 
                       12
                      /  \ 
                     8    15
                    /     /
                   4     13
                    \ 
                     7 
"""
A1 = AB(12)

A1.AjouterFD(15)
A1.AjouterFG(8)

A1.GetSAG().AjouterFG(4)
A1.GetSAG().GetSAG().AjouterFD(7)

A1.GetSAD().AjouterFG(13)


def CompteNoeud(A):
    """
     Retourne 1 si c est une feuille
    """
    if A.FD.EstVide() and A.FG.EstVide():
        print(A.GetRacine())
        return 1
    else:
        return 0

def ValeurFeuille(A):
    """
    Retourne la valeur d une feuille 
    """

    if A.FD.EstVide() and A.FG.EstVide():
        return A.GetRacine()
    else:
        return 0

    
def CompteFeuillePre(A):
    """
    Compte les feuilles d'un arbre binaire
    """
    if not A.EstVide() :
        n = CompteNoeud(A)
        n1 = CompteFeuillePre(A.FG)
        n2  = CompteFeuillePre(A.FD)
        return n + n1 + n2
    else:
        return 0


def SommeFeuillePre(A):
    """
    Somme (additionne) les valeurs des feuilles de l arbre binaire
    """
    if not A.EstVide() :
        n = ValeurFeuille(A)
        n1 = SommeFeuillePre(A.FG)
        n2  = SommeFeuillePre(A.FD)
        return n + n1 + n2
    else:
        return 0

    
print("###########Compte Feuille ##############")

print(CompteFeuillePre(A1))


print("###########Somme Feuille ##############")

print(SommeFeuillePre(A1))



# Exo 7
# Compte noeuds internes 
def CompteNoeudInterne(A):
    """
     Retourne 1 si c est un noeud interne 
    """
    if not A.FD.EstVide() or not  A.FG.EstVide():
        print("**",A.GetRacine(),"**")
        return 1
    else:
        return 0

    
def CompteNoeudInternePre(A):
    """
    Compte noeud interne d'un arbre binaire
    """
    if not A.EstVide() :
        n = CompteNoeudInterne(A)
        n1 = CompteNoeudInternePre(A.FG)
        n2  = CompteNoeudInternePre(A.FD)
        return n + n1 + n2
    else:
        return 0

    
print("###########Compte noeud interne##############")

print(CompteNoeudInternePre(A1))


    
# Exo 8
"""
d == droit
g == gauche 
1- q8(ab, 3, 1) = q8(g, 3,2) + q8(d, 3,2)
                = q8(gg, 3,3) + q8(gd, 3,3) + q8(dg, 3,3) +      q8(dd, 3,3)
                = 1 + 1 + 0 + 1
                = 3


2- q8(ab, 4, 1) = q8(g, 4,2) + q8(d, 4,2)
                = q8(gg, 4,3) + q8(gd, 4,3) + q8(dg, 4,3) +      q8(dd, 4,3)
                = q8(ggg, 4,4) + q8(ggd, 4,4) + q8(dgg, 4,4) +  q8(dgd, 4,4)  + q8(ddg, 4,4) +  q8(ddd, 4,4)
                = 1 + 0 + 1 + 1 + 1 + 1 

3- la fonction q8() compte le nombre de noeud au niveau <<n>> de l arbre 
"""
