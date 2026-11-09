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



