from afvlakking import aantal_vakjes


totalen = []
with open("invoer.txt")as invoer:
    eerste_getal = int(invoer.readline().strip())
    for i in range(eerste_getal):
        nieuwe_regel = invoer.readline().strip()
        getallen = [int(x) for x in nieuwe_regel.split()]
        aantal_vakjes(getallen[1:])
        print(aantal_vakjes((getallen[1:])))
        totalen.append(aantal_vakjes(getallen[1:]))

with open("uitvoer.txt", "w")as uitvoer:
    for i in range(len(totalen)):
        uitvoer.write(f"{i} {totalen[i]}")

