import random
f = open("cards.txt", "r")
karte=[]
ruka=""
brojac=0
for x in f:
      karte.append(x)

kartad=karte[random.randint(0,51)]
rukad=kartad
komanda="hit"
while (komanda=="hit"):
      karta=karte[random.randint(0,51)]
      while karta==kartad or karta[0] in ruka:
            karta=karte[random.randint(0,51)]
      ruka+=karta
      print("Ruka dealera:\n",rukad)
      print("Tvoja ruka:\n",ruka)
      if karta[0].isdigit():
            brojac+=int(karta[0])
      elif (karta[0]=="t"or"k"or"j"or"k"):
            brojac+=10
      elif karta[0]=="a":
            brojac+=11
      print("Bodovi:",brojac)
      komanda=input("hit or stand?\n")
      
