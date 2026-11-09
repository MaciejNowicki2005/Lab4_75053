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

