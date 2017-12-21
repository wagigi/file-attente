# Calcul de files d'attentes pour un modele M/M/C


def tempsmoyensysteme(alambda, mu, c):
    tq = tempsmoyenattente(alambda, mu, c)
    res = tq+(1/mu)
    return res


def nombremoysystem(alambda, mu, c):
    nq = nombremoyenfile(alambda, mu, c)
    res = nq + (alambda / mu)
    return res


def tempsmoyenattente(alambda, mu, c):
    p0 = probazero(alambda, mu, c)
    res = p0 * ((1 / (mu * c * (fact(c)) * ((1 - (alambda / (mu * c))) ** 2))) * ((alambda / mu) ** c))
    return res


def nombremoyenfile(alambda, mu, c):
    p0 = probazero(alambda, mu, c)
    res = p0 * ((alambda * mu * ((alambda / mu) ** c)) / ((fact(c - 1)) * ((c * mu) - alambda) ** 2))
    return res


def probaden(alambda, mu, c):
    p0 = probazero(alambda, mu, c)
    n = float(input("Entrez le n a chercher : "))
    choix = int(input("1 : Trouver 0 < n < C\n2 : Trouver n > C"))
    if choix == 1:
        res = p0 * (((alambda / mu) ** n) / fact(n))
        return res
    elif choix == 2:
        res = p0 * (((alambda / mu) ** n) / (fact(c) * (c ** (n - c))))
        return res
    else:
        probaden(alambda, mu, c)


def probazero(alambda, mu, c):
    n = 0
    cc = 0
    snc = 0
    while cc <= c - 1:
        snc += ((alambda / mu) ** n) / fact(n)
        n += 1
        cc += 1

    res = (1 / (snc + (((alambda / mu) ** c) / fact(c)) * ((1 - (alambda / (mu * c))) ** -1)))

    return res


def assezguichet(alambda, mu, c):
    res = alambda / (mu * c)
    return res < 1


def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)


def main():
    alambda = float(input("Entrer lambda (nb moyen d'arrive) : "))
    mu = float(input("Entrer mu (nb moyen de service) : "))
    c = int(input('Enter C : '))

    choix = int(
        input("Quelle opération ?\n1 : Temps moyen dans le système\n2 : Nombre moyen dans le système\n3 : Temps "
              "moyen d'attente dans la file\n4 : Nombvre moyen dans la file\n5 : Probabilite qu'il y ait n unité "
              "dans le système\n6 : P0\n7 : Assez de file pour pas d'engorgement?\nChoix : "))

    if choix == 1:
        print(tempsmoyensysteme(alambda, mu, c))
    elif choix == 2:
        print(nombremoysystem(alambda, mu, c))
    elif choix == 3:
        print(tempsmoyenattente(alambda, mu, c))
    elif choix == 4:
        print(nombremoyenfile(alambda, mu, c))
    elif choix == 5:
        print(probaden(alambda, mu, c))
    elif choix == 6:
        print(probazero(alambda, mu, c))
    elif choix == 7:
        print(assezguichet(alambda, mu, c))

    uia = input("Rerun ? Y/n")
    if uia == "y" or uia == "Y" and (uia != 'n' or uia != 'N'):
        main()
    else:
        exit(0)


if __name__ == '__main__':
    main()
