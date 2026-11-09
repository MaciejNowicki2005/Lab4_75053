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

