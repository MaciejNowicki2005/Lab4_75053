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



