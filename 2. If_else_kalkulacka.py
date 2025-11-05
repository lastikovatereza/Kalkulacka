
print("---------- Vítejte v Kalkulačce ----------")

a = float(input("Zde zadejte první číslo: "))
b = float(input("Zde zadejte druhé číslo: "))

print("1 - sčítání")
print("2 - odčítání")
print("3 - násobení")
print("4 - dělení")

operace = int(input("Vyber matematickou operaci (1-4): "))

if operace == 1:
    vysledek = a + b
elif operace == 2:
    vysledek = a - b
elif operace == 3:
    vysledek = a * b
elif operace == 4:
    if b != 0:
        vysledek = a / b
    else:
        print("Nulou nelze dělit!")
        vysledek = "N/A"

if operace > 0 and operace < 5:
    print(f"Výsledek: {vysledek}")
else:
    print("Neplatná volba")
print("Děkuji za použití kalkulačky.")