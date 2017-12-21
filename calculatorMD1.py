# Calcul de files d'attentes pour un modele M/D/1


def tempsmoyensysteme(alambda, mu):
    tq = tempsmoyenattente(alambda, mu)
    res = tq + (1 / mu)
    return res


def nombremoysystem(alambda, mu):
    nq = nombremoyenfile(alambda, mu)
    res = nq + (alambda / mu)
    return res


def tempsmoyenattente(alambda, mu):
    res = alambda / (2 * mu * (mu - alambda))
    return res


def nombremoyenfile(alambda, mu):
    res = (alambda ** 2) / (2 * mu * (mu - alambda))
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


def main():
    alambda = float(input("Entrer lambda (nb moyen d'arrive) : "))
    mu = float(input("Entrer mu (nb moyen de service) : "))
    choix = int(
        input("Quelle opération ?\n1 : Temps moyen dans le système\n2 : Nombre moyen dans le système\n3 : Temps "
              "moyen d'attente dans la file\n4 : Nombvre moyen dans la file\n5 : Probabilite qu'il y ait n unité "
              "dans le système\n6 : P0\n7 : Assez de file pour pas d'engorgement?\nChoix : "))

    if choix == 1:
        print(tempsmoyensysteme(alambda, mu))
    elif choix == 2:
        print(nombremoysystem(alambda, mu))
    elif choix == 3:
        print(tempsmoyenattente(alambda, mu))
    elif choix == 4:
        print(nombremoyenfile(alambda, mu))
    elif choix == 5:
        print("Non disponible en M/D/1")
    elif choix == 6:
        print("Non disponible en M/D/1")
    elif choix == 7:
        res = assezguichet(alambda, mu)
        print("Nombre guichet : {} resultat : {}".format(res[0], res[1]))

    uia = input("Rerun ? Y/n")
    if uia == "y" or uia == "Y" and (uia != 'n' or uia != 'N'):
        main()
    else:
        exit(0)


if __name__ == '__main__':
    main()
