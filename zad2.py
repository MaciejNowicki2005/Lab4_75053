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




