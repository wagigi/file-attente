# Calcul de files d'attentes pour un modele M/M/1/Q


def tempsmoyensysteme(alambda, mu):
    tq = tempsmoyenattente(alambda, mu)
    res = tq + (1 / mu)
    return res


def nombremoysystem(alambda, mu, q):
    divalmicr = alambda / mu
    res = divalmicr * (((1 - (q + 1) * (divalmicr ** q)) + (q * (divalmicr ** (q + 1)))) / (
            (1 - divalmicr) * (1 - (divalmicr ** (q + 1)))))
    return res


def tempsmoyenattente(alambda, mu, q):
    nq = nombremoyenfile(alambda, mu, q)
    res = nq/(alambda/(1-probaden(alambda, mu, n=q)))
    return res


def nombremoyenfile(alambda, mu, q):
    divalmicr = alambda / mu
    res = (divalmicr ** 2) * (((1 - (q * (divalmicr ** (q - 1)))) + ((q - 1) * (divalmicr ** q))) / (
            (1 - divalmicr) * (1 - (divalmicr ** (q + 1)))))
    return res


def assezguichet(alambda, mu):
    c = 0
    res = 2
    while res > 1:
        c += 1
        res = alambda / (mu * c)
    return c, res


def probaden(alambda, mu, n='x'):
    if n == 'x':
        n = float(input("n = ? "))
    else:
        n = float(n)
    res = (1-(alambda/mu))*((alambda/mu)**n)
    return res


def probazero(alambda, mu):
    n = 0
    res = (1-(alambda/mu))*((alambda/mu)**n)
    return res


def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)


def main():
    alambda = float(input("Entrer lambda (nb moyen d'arrive) : "))
    mu = float(input("Entrer mu (nb moyen de service) : "))
    q = float(input("Entrer Q (longueur de la file) : "))
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
    if uia != 'n' or uia != 'N':
        main()
    else:
        exit(0)


if __name__ == '__main__':
    main()
