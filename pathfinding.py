# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 09:23:01 2014

@author: Nicolas Sobczak
"""

# import des modules
import pathfinding_stack
import random


# %% _________________________________________________________________________
##########################
# Parcours du labyrinthe #
##########################

def laby(lstVoisins):
    # Initialisation

    lstCasVis = [(0 == 1) for i in range(len(lstVoisins))]  # liste des cases visitées
    lstCasVis

    piloche = pathfinding_stack.creerPile()  # pile emmagasinant les cases correspondantes au bon parcours
    pileChoix = pathfinding_stack.creerPile()  # utile pour connaitre la case de retour en cas de cul de sac

    caseR = 1  # numéro réel de la case, ici la 1ere case
    caseF = caseR - 1  # numéro fictif de la case, ici l'entrée du labirynthe
    derniereCase = len(lstVoisins) - 1

    piloche = pathfinding_stack.empiler(piloche, caseR)  # la première case de la pile est forcément 1

    # Hérédité
    while not lstCasVis[derniereCase]:

        # Avancée sans choix, une seule case possible
        if len(lstVoisins[caseF]) == 2:
            lstCasVis[caseF] = 1 == 1

            # Case 1 à plusieurs cases adjacentes
            if caseF == 0:
                pileChoix = pathfinding_stack.empiler(pileChoix, caseF)
                caseR = random.choice(lstVoisins[caseF])
                while lstCasVis[caseR - 1]:
                    caseR = random.choice(lstVoisins[caseF])
                piloche = pathfinding_stack.empiler(piloche, caseR)
                caseF = caseR - 1

                # Toutes les autres cases
            else:
                a = lstVoisins[caseF][0] - 1
                if lstCasVis[a]:
                    x = 1
                else:
                    x = 0
                caseR = lstVoisins[caseF][x]
                piloche = pathfinding_stack.empiler(piloche, caseR)
                caseF = caseR - 1

        # Choix possible entre plusieurs cases
        if len(lstVoisins[caseF]) > 2:
            lstCasVis[caseF] = 1 == 1
            caseDispo = (1 == 0)
            for i in range(len(lstVoisins[caseF])):
                j = lstVoisins[caseF][i]
                if not lstCasVis[j - 1]:
                    caseDispo = (1 == 1)

            if caseDispo:
                pileChoix = pathfinding_stack.empiler(pileChoix, caseF)
                caseR = random.choice(lstVoisins[caseF])
                while lstCasVis[caseR - 1]:
                    caseR = random.choice(lstVoisins[caseF])
                piloche = pathfinding_stack.empiler(piloche, caseR)
                caseF = caseR - 1

            else:
                pileChoix = pathfinding_stack.depiler(pileChoix)
                caseF = pathfinding_stack.sommet(pileChoix)
                while pathfinding_stack.sommet(piloche) != (caseF + 1):
                    piloche = pathfinding_stack.depiler(piloche)

        # Cul de sac et 1ère et dernière cases
        if len(lstVoisins[caseF]) == 1:
            lstCasVis[caseF] = 1 == 1

            # 1ère et dernière cases
            if caseF == 0 or caseF == derniereCase:
                caseR = lstVoisins[caseF][0]
                if caseF == 0:
                    piloche = pathfinding_stack.empiler(piloche, caseR)
                caseF = caseR - 1

                # Cul de sac
            else:
                caseF = pathfinding_stack.sommet(pileChoix)
                while pathfinding_stack.sommet(piloche) != (caseF + 1):
                    piloche = pathfinding_stack.depiler(piloche)

    # Resultat
    res = []
    while not pathfinding_stack.pileVide(piloche):
        res = [pathfinding_stack.sommet(piloche)] + res
        piloche = pathfinding_stack.depiler(piloche)

    return (print("a possible way to escape is :", res))


# %%__________________________________________________________________________________________________
# ____________________________________________________________________________________________________
def monMain():
    # liste des cases accessibles à partir de chaque case

    # création d'un labyrinthe 3X6
    lstVoisins1 = [[7], [3], [2, 9], [5], [4, 11, 6], [5, 12], \
                   [1, 8, 13], [7, 14], [15, 3, 10], [16, 9], [17, 5], [6, 18], \
                   [7], [8, 15], [14, 9], [10, 17], [16, 11], [12]]

    # création d'un labyrinthe 4X4
    lstVoisins2 = [[5], [3, 6], [2, 4], [3], \
                   [1, 6], [5, 2, 7, 10], [6], [12], \
                   [13], [6, 11, 14], [10, 12], [11, 8, 16], \
                   [9, 14], [10, 13, 15], [14], [12]]

    # création d'un labyrinthe 5X5
    lstVoisins3 = [[6], [7], [8], [5], [10], \
                   [1, 7], [6, 2, 8], [3, 7, 13], [14, 10], [9, 5], \
                   [12, 16], [11, 13], [12, 8, 14], [13, 9, 19, 15], [14, 20], \
                   [11, 21], [22, 18], [17, 19, 23], [14, 18], [15], \
                   [16], [17], [18, 24], [23, 25], [24]]

    # création d'un labyrinthe 3X5 à 2 solutions
    lstVoisins4 = [[6], [7, 3], [2, 4, 8], [3, 5], [4], \
                   [1, 7, 11], [6, 2, 12], [3, 9, 13], [8, 14, 10], [9, 15], \
                   [6], [7, 13], [12, 8], [9], [10]]

    # création d'un labyrinthe 3X5 à plus de 2 solutions
    lstVoisins5 = [[6], [7, 3], [2, 4, 8], [3, 5, 9], [4, 10], \
                   [1, 11], [2, 12], [3, 13], [4, 14], [5, 15], \
                   [6, 12], [7, 11, 13], [12, 8, 14], [9, 13], [10]]

    # création d'un labyrinthe 2X4
    lstVoisins6 = [[2, 5], [1], [4, 7], [3, 8], \
                   [1, 6], [5, 7], [6, 3], [4]]

    # création du labyrinthe 4X4
    lstVoisins7 = [[2], [1, 6], [4], [3, 8], [9], [2, 7], [6, 8], [4, 7, 12], [10, 13, 5], \
                   [9], [12, 15], [8, 11], [9, 14], [13, 15], [11, 14, 16], [15]]

    # Tests Unitaires
    laby(lstVoisins1)
    laby(lstVoisins2)
    laby(lstVoisins3)
    laby(lstVoisins4)
    laby(lstVoisins5)
    laby(lstVoisins6)
    laby(lstVoisins7)


if __name__ == "__main__":
    monMain()
