from noeud import Noeud

print('-'.join(['1', '2', '3', '4']))

deux = Noeud(2)
y = Noeud("y")

addition = Noeud("+")

addition.ajouter_enfants(deux)
addition.ajouter_enfants(y)

exp = Noeud("exp")

exp.ajouter_enfants(addition)

exp.afficher()
print()
print(exp.evaluer({"y": 3}))

exp.tracer("y", [-2, -1, 0, 1, 2])


