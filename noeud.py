import math
import matplotlib.pyplot as plt
"""
Classe représentant un nœud dans un arbre d'expression.
"""
class Noeud:
    def __init__(self,valeur):
        self.valeur = valeur
        self.enfants = []

    def ajouter_enfants(self,enfants):
        self.enfants.append(enfants)

    def afficher(self):   

        for enfants in self.enfants:
            enfants.afficher()

        """if len(self.enfants==2):
            enfant1 = self.enfants[0]
            enfant2 = self.enfants[1]
            print(self.valeur+"("+enfant1.affciher()+","+enfant2.afficher()+")")
        elif len(self.enfants==1):
            print(self.)"""



    def evaluer(self,valeurs):

        if isinstance(self.valeur,(int,float)):
            return float(self.valeur)
        elif self.valeur == "+":
            return self.enfants[0].evaluer(valeurs) + self.enfants[1].evaluer(valeurs)
        elif self.valeur == "-":
            return self.enfants[0].evaluer(valeurs) - self.enfants[1].evaluer(valeurs)
        elif self.valeur == "*":
            return self.enfants[0].evaluer(valeurs) * self.enfants[1].evaluer(valeurs)
        elif self.valeur == "/":
            return self.enfants[0].evaluer(valeurs) / self.enfants[1].evaluer(valeurs)
        elif self.valeur == "exp":
            return math.exp(self.enfants[0].evaluer(valeurs))
        elif self.valeur == "log":
            return math.log(self.enfants[0].evaluer(valeurs))
        elif self.valeur == "sin":
            return math.sin(self.enfants[0].evaluer(valeurs))
        elif self.valeur == "cos":
            return math.cos(self.enfants[0].evaluer(valeurs))
        elif self.valeur not in valeurs:
            raise ValueError("Valeur manquante pour "+ self.valeur)
        return float(valeurs[self.valeur])
            
    def tracer(self,variable,liste):
        resultats = []

        for valeur in liste : 
            res = self.evaluer({variable : valeur})
            resultats.append(res)

        plt.plot(liste,resultats)
        plt.xlabel(variable)
        plt.ylabel("f("+variable+")")
        plt.grid()
        plt.show()

    
