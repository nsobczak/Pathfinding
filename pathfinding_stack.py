# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 14:25:25 2014

@author: Nicolas Sobczak

FICHIER A ENREGISTRER DANS LE REPERTOIRE DE TRAVAIL
"""


# %% __________________________________________________________
# def de l'objet pile et de ses fonctions

def creerPile():
    return ([])


def empiler(pile, elm):
    return (pile + [elm])


def depiler(pile):
    return (pile[:-1])


def sommet(pile):
    return (pile[-1])


def pileVide(pile):
    return (pile == [])
