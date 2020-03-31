import random
f = open("cards.txt", "r")
karte=[]
ruka=""
brojac=0
for x in f:
      karte.append(x)

komanda="hit"
while (komanda=="hit"):
      karta=karte[random.randint(0,51)]
      ruka+=karta
      print(ruka)
      if ruka[0].isdigit():
            brojac+=int(ruka[0])
            print(brojac)
      komanda=input("hit or fold?\n")
      
  
