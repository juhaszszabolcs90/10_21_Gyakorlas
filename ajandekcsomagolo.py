"""
1. Feladat: Ajándékcsomagoló szalag számítás
Készítsünk programot, amely ajándékok csomagolásához szükséges szalag hosszát számolja ki.
A szalag hosszának úgy kell elegendőnek lennie, hogy kétszer körbeérje az ajándék körvonalát (téglalap alapú csomag esetén),
és a masni készítéséhez további 50 cm szükséges.
A program kérje be az ajándék hosszát, szélességét és magasságát (cm-ben), az ajándékok számát, valamint a rendelkezésre
álló szalag hosszát (méterben).
Számítsa ki, hogy hány méter szalagra van szükség a megadott számú ajándék csomagolásához, és közölje a felhasználóval,
hogy elegendő-e a szalag.
"""
def festekszamlalo():
	hossz = float(input("Kérlek add meg a doboz hosszát (pl. 10.1) cm-ben: "))
	szelesseg = float(input("Kérlek add meg a doboz szélességét (pl. 10.1) cm-ben: "))
	magassag = float(input("Kérlek add meg a doboz magasságát (pl. 10.1) cm-ben: "))
	szalag_hossza = float(input("Kérlek add meg a rendelkezésre álló szalag hosszát (pl. 10.1) m-ben: "))
	ajandekok_szama = int(input("Kérlek add meg az ajándékok számát: "))

	kerulet1 = (szelesseg + magassag) * 2
	kerulet2 = (hossz + magassag) * 2

	szalag_egy_ajandekra = kerulet1 + kerulet2 + 50

	szukseges_szalag_cmben = szalag_egy_ajandekra * ajandekok_szama
	szukseges_szalag_meterben = szukseges_szalag_cmben / 100

	print(f"Az ajándékok csomagolásához szükséges szalag {szukseges_szalag_meterben} méter")

	if szalag_hossza < szukseges_szalag_meterben:
		print(f"A rendelkezésre álló szalag nem elegendő. Szükség van még {szukseges_szalag_meterben-szalag_hossza} m-re")
	else:
		print("A rendelkezésre álló szalag ELEGENDŐ.")


festekszamlalo()