import random
f = open("cards.txt", "r")
karte=[]
ruka=""
brojac=0
brojacd=0
for x in f:
      karte.append(x)

kartad=karte[random.randint(0,50)]
rukad=kartad
komanda="hit"
while (komanda=="hit"):
      karta=karte[random.randint(0,50)]
      while karta==kartad or karta[0] in ruka:
            karta=karte[random.randint(0,50)]
      ruka+=karta
      print("Ruka dealera:\n",rukad)
      print("Tvoja ruka:\n",ruka)
      if karta[0].isdigit():
            brojac+=int(karta[0])
      elif karta[0]=="t"or"k"or"j"or"q":
            brojac+=10
      elif karta[0]=="a":
            brojac+=11
      #print("Bodovi:",brojac)
      if brojac>21:
            print ("izgubio si!!!")
            exit()
      komanda=input("hit or stand?\n")
if kartad[0].isdigit():
      brojacd+=int(kartad[0])
elif kartad[0]=="t"or"k"or"j"or"q":
      brojacd+=10
elif kartad[0]=="a":
      brojacd+=11
while brojacd<11:
      kartad=karte[random.randint(0,50)]
      rukad+=kartad
      if kartad[0].isdigit():
            brojacd+=int(kartad[0])
      elif kartad[0]=="t"or"k"or"j"or"q":
            brojacd+=10
      elif kartad[0]=="a":
            brojacd+=11
#print("Bodovi dealera:", brojacd)
print("Tvoja ruka:\n",ruka)
print("Ruka dealera:\n", rukad)
if brojac>brojacd:
      print("dobio si")
else:
      print("izgubio si")



            
