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





