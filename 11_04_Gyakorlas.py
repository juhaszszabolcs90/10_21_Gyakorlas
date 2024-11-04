"""1. Egyszerű számbekérő
Kérj be egy számot a felhasználótól, és döntsd el, hogy páros vagy páratlan. Írd ki az eredményt!”””
"""
def elso_feladat():
    user_input = int(input("kérlek adj meg egy számot! "))
    if user_input % 2 == 0:
        print(f"A {user_input} szám PÁROS")
    else:
        print(f"A {user_input} szám NEM PÁROS = PÁRATLAN")


"""
2. Összegszámítás
Kérj be egy egész számot, és számítsd ki az 1-től a megadott számig terjedő egész számok összegét.
"""
def masodik_feladat():
    sum_ = 0
    user_input = int(input("kérlek adj meg egy számot! "))
    for i in range(1, user_input+1):
        sum_ += i
    print(sum_)


"""
3. Számok listázása és összegzése
Írj egy programot, amely bekér  n számot a felhasználótól, majd egy while ciklussal megkérdezi a felhasználót, hogy szeretne-e újabb számot megadni. Addig folytassa a program a számok bekérését, amíg a felhasználó igennel válaszol. A program végén jelenítse meg a bekért számok összegét.
b) jelenítse meg a bekért számokat (lista használata)


"""


"""
4. Két szám közötti számok
Kérj be két számot a felhasználótól (a és b). Írasd ki az összes számot a és b között.
b) Ha a nagyobb, mint b, akkor csökkenő sorrendben írasd ki őket.
"""




"""
5. Egyszerű jelszókérés
Készíts egy programot, amely egy előre meghatározott jelszót vár el a felhasználótól. A program addig kérdez, amíg a helyes jelszót meg nem adják. Ha eltalálja a jelszót, jelenjen meg egy üzenet, hogy „Sikeres belépés”.
"""


"""
6. Szorzótábla
Írasd ki egy adott szám szorzótábláját 1-től 10-ig. Például, ha a felhasználó 5-öt ad meg, akkor az eredmény legyen:
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
"""


"""
7. Maximum keresés lista elemeiben
Készíts egy programot, amely bekér 5 számot a felhasználótól, és kiírja a legnagyobb számot. A programban használj egy for ciklust a számok bekérésére, és egy if feltételt a legnagyobb szám megkeresésére.
"""


"""
8. Prímszám ellenőrzés
Kérj be egy számot, és döntsd el, hogy prímszám-e vagy sem. A program akkor jelezze, ha prímszámot talált, és akkor is, ha nem az.
"""


"""
9. Piramis rajzolása csillagokkal
Kérj be egy számot, amely megadja a piramis magasságát, majd rajzolj ki egy csillagpiramist ennek megfelelően. Például egy 5 magas piramis:
   *
   ***
  *****
 *******
*********


"""


"""
10. Szorzótábla mátrix formában
Készíts egy programot, amely kiírja az 1-től 10-ig terjedő szorzótáblát egy 10x10-es mátrix formájában. Minden sor egy-egy i értéket képviseljen, minden oszlop pedig egy j értéket, és az i * j szorzatot jelenítse meg.
"""

# elso_feladat()
# masodik_feladat()