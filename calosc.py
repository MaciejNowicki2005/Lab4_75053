#Zadanie 1
moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
print(f"Zdefiniowana lista statycznie: {moja_lista}")

print(f"Odwołanie do elementu pierwszego listy, od początku: {moja_lista[0]}\nOd końca: {moja_lista[-1]}")

print(f"Ilość elementów w liście: {len(moja_lista)}")

print(f"Element największy: {max(moja_lista)}\nElement najmniejszy: {min(moja_lista)}")

print(f"Suma wartości w liście: {sum(moja_lista)}")

print(f"Lista posortowana: {sorted(moja_lista)}")

moja_lista.append(67)
print(f"Lista po dodaniu 67:{moja_lista}")

moja_lista.insert(0,231)
print(f"Lista po wstawieniu na pierwsze miejsce (indeks zerowy) elementu o wartości 231:{moja_lista}")

print(f"Zwrócimy i usuniemy pierwszy element w liście, zwrócono element: {moja_lista.pop(0)}\nLista po usunięciu elementu o indeksie 0:{moja_lista}")

moja_lista.reverse()
print(f"Lista po odwróceniu: {moja_lista}")

listaDruga = ["Facebook","TikTok","Messenger","Instagram"]
listaLaczona = []
listaLaczona = listaDruga + moja_lista
print(f"Połączenie obu list w jedną:{listaLaczona}")

listaMnoga = listaDruga * 2
print(f"Lista wyświetlana podwójnie:{listaMnoga}")

print("Z listy łaczonej elementy od początku do elementu o indeksie n-tym:")
n = int(input("Podaj n:"))
print(listaLaczona[:n])

print("Z listy łaczonej elementy od indeksu n-tego do konca:")
n = int(input("Podaj n:"))
print(listaLaczona[n:])

print("Z listy łączonej, od indeksu m-tego, do n-tego co wartość k:")
m = int(input("Podaj m:"))
n = int(input("Podaj n:"))
k = int(input("Podaj k:"))
print(listaLaczona[m:n:k])

print("Odpowiednik 'reverse' na wycinkach:")
print(listaLaczona[::-1])


#Zadanie 2
def dodajOsoby(ile):
    imiona = []
    for osoba in range(ile):
        osoba = input("Podaj osobę do listy: ")
        imiona.append(osoba)
    return imiona

imiona = dodajOsoby(4)
imiona.sort()
print(f"Lista posortowana alfabetycznie: {imiona}")


imiona = imiona + dodajOsoby(2)
print(f"Pobieramy osobę {imiona.pop()},bez niej wygląda to już tak: {imiona}")

imiona.insert(2, str(input("Dodaj kolejną osobę, będzie ona na trzeciej pozycji:")))
print(f"Lista osób po dodaniu nowej na pozycji 3-ciej: {imiona}")

imiona.reverse()
print(f"Lista osob po odwróceniu kolejności: {imiona}")

imiona = imiona * 2
print(f"Lista osób po zdublowaniu jej: {imiona}")

#Zadanie 3
imie = str(input("Podaj swoje imię:"))
print(f"Witaj, {imie}")

wiek = str(input("Podaj swoje wiek:"))
print(f"Twój wiek to {wiek}")

imie = str(input("Podaj swoje imie:"))
nazwisko = str(input("Podaj swoje nazwisko:"))
inicjaly = imie[:1] + nazwisko[:1]
print(f"Twoje inicjały to: {inicjaly}")

lancuch = str(input("Podaj jakiś łańcuch znaków:"))
print(lancuch*5)

lancuch1 = str(input("Podaj łańcuch 1: "))
lancuch2 = str(input("Podaj łańcuch 2: "))
lancuchyPolaczone = lancuch1+lancuch2
print(f"Połączone oba łańcuchy to: {lancuchyPolaczone}")

ciag1 = str(input("c1: "))
ciag2 = str(input("c2: "))

ciag3 = ciag1[0:int(len(ciag1)/2)] + ciag2[int(len(ciag2)/2):int(len(ciag2))]
print(ciag3)

#Zadanie 4

zdanie = input("Podaj zdanie: ").lower()

alfabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

obecne = []
brakujace = []

for znak in zdanie:
    if znak in alfabet:
        obecne.append(znak)

obecne = sorted(obecne)
print(f"Litery alfabetycznie: {obecne}")

for znak in alfabet:
    if znak not in zdanie:
        brakujace.append(znak)
print(f"Brakujące litery: {brakujace}")

#Zadanie 5
dniTygodnia = ("Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota","Niedziela")
print(f"Krotka z dniami tygodnia {dniTygodnia}")

#Zadanie 6
owoce = ('jabłko', 'banan', 'gruszka', 'banan', 'banan', 'malina')

print(f"Banan w krotce występuje: {owoce.count('banan')} razy")

#Zadanie 7
mojaKrotka = (10, 2, 6, 6, 9, 13, 0, 1)
print(f"Moja krotka przed sortowaniem: {mojaKrotka}")

listaPomocnicza = []
for liczba in mojaKrotka:
    listaPomocnicza.append(liczba)

listaPomocnicza.sort()

mojaKrotka = ()
for liczba in listaPomocnicza:
    mojaKrotka += (liczba,)

print(f"Moja krotka po sortowaniu: {mojaKrotka}")
print(f"Typ mojaKrotka: {type(mojaKrotka)}")

#Zadanie 8
stopnie = ("Szeregowy","Kapral","Sierżancie","Porucznik","Kapitan","Major","Pułkownik")
ilosc_stopni = len(stopnie)

print(f"Ilość stopni: {ilosc_stopni}")

major_index = stopnie.index("Major")
print(f"Indeks na którym znajduje się major: {major_index}")

pulkownik_wystepuje = "Nie"
for stopien in stopnie:
    if stopien=="Pułkownik":
        pulkownik_wystepuje = "Tak"
        break
    else:
        continue
print(f'Pułkownik występuje? {pulkownik_wystepuje} ')



#Zadanie 9
listaZakupow = {
    "PS5": 4999.99,
    "Grand Theft Auto: VI": 599.99 ,
    "Kontroler": 229.99 ,
    "Stacja ładująca": 339.99,
    "Słuchawki": 249.99
}

print("Lista zakupów:")
for artykul, kwota in listaZakupow.items():
    print(f"{artykul}: {kwota} PLN")

print(f"Łączne wydatki: {sum(listaZakupow.values())} PLN")