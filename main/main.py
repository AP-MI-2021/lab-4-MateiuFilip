def citire_lista():
    '''
    :return: lista citita
    '''
    l = []
    n = int(input("Introduceti numar de elemente: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l


def prim(a):
    '''
    Functie ce verifica daca a este prim
    :param a: numar intreg
    :return: daca a este prim
    '''
    if a == 1 or a == 0:
        return False
    else:
        for i in range(2, a):
            if a % i == 0 and i != a:
                return False
        return True


def numere_prime_din_lista(l):
    '''
    Functie ce returneaza numerele neprime dintr-o lista
    :param l: lista data
    :return: numerele neprime dintr-o lista
    '''
    sir_numere_prime = []
    for x in l:
        if prim(x) == 0:
            sir_numere_prime.append((x))
    return sir_numere_prime


def test_numere_prime_din_lista():
    '''

    Functie ce verifica eficienta lui numere_prime_din_lista()
    '''
    assert numere_prime_din_lista([1, 2, 3]) == [1]
    assert numere_prime_din_lista([1, 3, 5, 6]) == [1, 6]
    assert numere_prime_din_lista([7, 8, 9]) == [8, 9]


def media_aritmetica_lista_comparata_cu_n(l, n):
    '''
    Verifica dacă media aritmetică a numerelor este mai mare decât un număr n dat
    :param l: lista data
    :param n: numarul care se compara cu media aritmetica a listei
    :return: dacă media aritmetică a numerelor este mai mare decât un număr n dat
    '''
    suma = 0
    for x in l:
        suma = suma + x
    mediaaritm = suma / len(l)
    if mediaaritm > int(n):
        return "DA"
    return "NU"


def test_media_aritmetica_lista_comparata_cu_n():
    '''
    Functie care verifica daca media aritmetica a numerelor este mai mare decât un număr n dat
    :return: daca media aritmetica a numerelor este mai mare decât un număr n dat
    '''
    assert media_aritmetica_lista_comparata_cu_n([10, -3, 25, -1, 3, 25, 18], 10) == "DA"
    assert media_aritmetica_lista_comparata_cu_n([10, 13, 14], 21) == "NU"
    assert media_aritmetica_lista_comparata_cu_n([192, 19], 30) == "DA"


def nr_divizori_proprii(a):
    nr_div = 0
    for i in range(2, a):
        if a % i == 0 and i != a:
            nr_div = nr_div + 1
    return nr_div


def lista_dupa_adaugarea_nr_de_divizori(l):
    '''
    Functie care returneaza lista prin adăugarea după fiecare element numărul de divizori proprii ai elementului
    :param l: lista data
    :return: lista prin adăugarea după fiecare element numărul de divizori proprii ai elementului
    '''
    lista_cu_elemente_divizori = []
    for x in l:
        lista_cu_elemente_divizori.append(x)
        lista_cu_elemente_divizori.append(nr_divizori_proprii(x))
    return lista_cu_elemente_divizori


def test_lista_dupa_adaugarea_nr_de_divizori():
    assert lista_dupa_adaugarea_nr_de_divizori([19]) == [19, 0]
    assert lista_dupa_adaugarea_nr_de_divizori([1, 2, 3]) == [1, 0, 2, 0, 3, 0]
    assert lista_dupa_adaugarea_nr_de_divizori([4, 9]) == [4, 1, 9, 1]


def main():
    l = []
    test_numere_prime_din_lista()
    test_media_aritmetica_lista_comparata_cu_n()
    test_lista_dupa_adaugarea_nr_de_divizori()
    while True:
        print("1.Citire lista.")
        print("2.Afișarea listei după eliminarea numerelor prime din listă.")
        print("3.Afiseaza dacă media aritmetică a numerelor este mai mare decât un număr n dat.")
        print("4.Afișeaza lista prin adăugarea după fiecare element numărul de divizori proprii ai elementului")
        print("5.")
        print("-1.Inchide Programul.")
        optiune = input("Dati optiune: ")

        if optiune == "1":
            l = citire_lista()

        elif optiune == "2":
            print(numere_prime_din_lista(l))

        elif optiune == "3":
            n = input("Introdu parametru: ")
            print(media_aritmetica_lista_comparata_cu_n(l, n))
        elif optiune == "4":
            print(lista_dupa_adaugarea_nr_de_divizori(l))
        elif optiune == "5":
            print()
        elif optiune == "-1":
            print("La revedere!")
            break
        else:
            print("Optiune invalida.")


main()
