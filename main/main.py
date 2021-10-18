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
    '''
    Returneaza numarul de divizori proprii ai lui a
    :param a: numar al listei
    :return: numarul de divizori proprii ai lui a
    '''
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
    '''
    Verifica eficienta functiei lista_dupa_adaugarea_nr_de_divizori()
    '''
    assert lista_dupa_adaugarea_nr_de_divizori([19, 22, 31]) == [19, 0, 22, 2, 31, 0]
    assert lista_dupa_adaugarea_nr_de_divizori([1, 2, 3, 5]) == [1, 0, 2, 0, 3, 0, 5, 0]
    assert lista_dupa_adaugarea_nr_de_divizori([4, 9]) == [4, 1, 9, 1]
def numar_aparente(x,l):
    '''

    :param x: numarul prelucrat
    :param l: lista data
    :return: numarul de aparitii a lui x in l
    '''
    numar=0
    for i in l:
        if i == x:
            numar=numar+1
    return numar
def triplet(x,i,l):
    '''

    :param x: numar dat
    :param i: indexului lui x
    :param l: lista data
    :return: tripletul elementului x
    '''
    lista=[]
    lista.append((x))
    lista.append((i))
    lista.append(numar_aparente(x,l))
    return  lista


def liste_tripleti(l):
    '''

    :param l: lista prelucrata
    :return: lista noua in care fiecare element a fost inlocuit cu un triplet
    '''
    lista_tripleti=[]
    for i in range(len(l)):

        lista_tripleti.append((triplet(l[i],i,l)))
    return lista_tripleti


def test_liste_tripleti():
    '''
    Verifica eficienta functiei liste_tripleti()
    '''
    assert liste_tripleti([25, 13, 26, 13])== [[25, 0, 1], [13, 1, 2], [26, 2, 1], [13, 3, 2]]
    assert liste_tripleti([1,2,3,4,5,1]) == [[1, 0, 2], [2, 1, 1], [3, 2, 1], [4, 3, 1], [5, 4, 1], [1, 5, 2]]
    assert liste_tripleti([12,13,14,15,12,13,14]) == [[12, 0, 2], [13, 1, 2], [14, 2, 2], [15, 3, 1], [12, 4, 2], [13, 5, 2], [14, 6, 2]]

def main():
    l = []
    test_numere_prime_din_lista()
    test_media_aritmetica_lista_comparata_cu_n()
    test_lista_dupa_adaugarea_nr_de_divizori()
    test_liste_tripleti()
    while True:
        print("1.Citire lista.")
        print("2.Afișarea listei după eliminarea numerelor prime din listă.")
        print("3.Afiseaza dacă media aritmetică a numerelor este mai mare decât un număr n dat.")
        print("4.Afișeaza lista prin adăugarea după fiecare element numărul de divizori proprii ai elementului")
        print("5.Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un tuplu în care pe")
        print("prima poziție este numărul, pe a doua poziție va fi indexul elementului din listă, iar pe a treia")
        print("poziție apare numărul de apariții a numărului.")
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
            print(liste_tripleti(l))
        elif optiune == "-1":
            print("La revedere!")
            break
        else:
            print("Optiune invalida.")


main()
