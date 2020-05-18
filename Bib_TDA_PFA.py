##--------------------------------------------------
##     Bibliothèque TDA Piles - Files - Arbres
##--------------------------------------------------

##--------------------------------------------------
##     Piles 
##--------------------------------------------------
class Pile:
    def __init__(self):
        self.items = []

    def EstVide(self):
        return self.items == []

    def Ajouter(self, item):
        self.items.append(item)

    def Retirer(self):
        return self.items.pop()

    def Premier(self):
        return self.items[len(self.items)-1]

    def AffichePile(self):
        print(self.items)

        
##--------------------------------------------------
##     Files 
##--------------------------------------------------
class File:
    def __init__(self):
        self.items = []

    def EstVide(self):
        return self.items == []

    def Ajouter(self, item):
        self.items.insert(0,item)

    def Retirer(self):
        return self.items.pop()

    def Premier(self):
        return self.items[len(self.items)-1]
       
##--------------------------------------------------
##     Arbres Binaires : AB 
##--------------------------------------------------
class AB:
    def __init__(self,racine=None):
        self.val = racine
        if racine == None:
            self.FG = None
            self.FD = None
        else:          
            self.FG = AB()
            self.FD = AB()
   
    def SetRacine(self,element):
        if self.val == None:
            self.val = element
            self.FG = AB()
            self.FD = AB()

    def AjouterFG(self,element):
        if type(AB())==type(element):
            self.FG = element
        else:
            self.FG = AB(element)
    
    def AjouterFD(self,element):
        if type(AB())==type(element):
            self.FD = element
        else:
            self.FD = AB(element)
    
#    def AjouterSAG(self,arb):
#        self.FG = arb
#
#    def AjouterSAD(self,arb):
#        self.FD = arb

    def EstVide(self):
        if self==None:
            return True
        else:
            return self.val == None         
    
    def GetSAG(self):
        return self.FG

    def GetSAD(self):
        return self.FD

    def GetRacine(self):
        return self.val

