# coding=utf-8
# Calcul de files d'attentes pour un modele M/M/1

import math


def tempsmoyensysteme(alambda, mu):
    res = 1 / (mu - alambda)
    return res


def nombremoysystem(alambda, mu):
    res = alambda / (mu - alambda)
    return res


def tempsmoyenattente(alambda, mu):
    res = alambda / (mu * (mu - alambda))
    return res


def nombremoyenfile(alambda, mu):
    res = (alambda ** 2) / (mu * (mu - alambda))
    return res


def probaden(alambda, mu):
    n = float(input("n = ? "))
    res = (1 - (alambda / mu)) * ((alambda / mu) ** n)
    return res


def probazero(alambda, mu):
    n = 0
    res = (1 - (alambda / mu)) * ((alambda / mu) ** n)
    return res


def assezguichet(alambda, mu):
    c = 0
    res = 2
    while res > 1:
        c += 1
        res = alambda / (mu * c)
    return c, res


def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)


def tempssup(alambda, mu):
    T = float(input("Quelle valeur de T : "))
    res = (alambda / mu) * math.exp(-(mu - alambda) * T)
    return res


def main():
    alambda = float(input("Entrer lambda (nb moyen d'arrive) : "))
    mu = float(input("Entrer mu (nb moyen de service) : "))

    choix = int(
        input("Quelle opération ?\n1 : Temps moyen dans le système\n2 : Nombre moyen dans le système\n3 : Temps "
              "moyen d'attente dans la file\n4 : Nombvre moyen dans la file\n5 : Probabilite qu'il y ait n unité "
              "dans le système\n6 : P0\n7 : Assez de file pour pas d'engorgement?\n8 : Temps d'attente superieur a :\nChoix : "))

    if choix == 1:
        print(tempsmoyensysteme(alambda, mu))
    elif choix == 2:
        print(nombremoysystem(alambda, mu))
    elif choix == 3:
        print(tempsmoyenattente(alambda, mu))
    elif choix == 4:
        print(nombremoyenfile(alambda, mu))
    elif choix == 5:
        print(probaden(alambda, mu))
    elif choix == 6:
        print(probazero(alambda, mu))
    elif choix == 7:
        res = assezguichet(alambda, mu)
        print("Nombre guichet : {} resultat : {}".format(res[0], res[1]))
    elif choix == 8:
        print(tempssup(alambda, mu))

    uia = input("Rerun ? Y/n")
    if uia != 'n' or uia != 'N':
        main()
    else:
        exit(0)


if __name__ == '__main__':
    main()
