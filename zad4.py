
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




