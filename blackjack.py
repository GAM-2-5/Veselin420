#otvaram tekst file s kartama u obliku stringova i tu drzim varijable
import random
f = open("cards.txt", "r")
karte=[]
ruka=""
rukad="nepoznate dvije karte"
brojac=0
brojacd=0
for x in f:
      karte.append(x)
#while za uzimanje karata igraca
komanda="hit"
while (komanda=="hit"):
      karta=karte[random.randint(0,50)]
      while karta==karta[0] in ruka: #provjeravam da se uzeta karta ne ponavlja
            karta=karte[random.randint(0,50)]
      ruka+=karta
      #ispis ruku
      print("Ruka dealera:\n",rukad)
      print("Tvoja ruka:\n",ruka)
      #dodavanje bodova u ovisnosti od vrijednosti uzete karte
      if karta[0].isdigit(): 
            brojac+=int(karta[0])
      elif karta[0]=="t"or"k"or"j"or"q":
            brojac+=10
      elif karta[0]=="a":
            brojac+=11
      #print("Bodovi:",brojac) 
      if brojac>21: #ako igrac povuce vise od 21 bodova
            print ("izgubio si!!!")
            exit()
      komanda=input("hit or stand?\n")
#ponavljam sve isto, ali za dealera. Ovaj dio iznad while-a za dealera se odnosi na kartu iznad prvog while-a.
rukad=""
while brojacd<13:
      kartad=karte[random.randint(0,50)]
      while ruka.count(kartad)==1 or rukad.count(kartad)==1: #provjeravam da se ne ponavlja
            kartad=karte[random.randint(0,50)]
      rukad+=kartad
      if kartad[0].isdigit():
            brojacd+=int(kartad[0])
      elif kartad[0]=="t"or"k"or"j"or"q":
            brojacd+=10
      elif kartad[0]=="a":
            brojacd+=11
#print("Bodovi dealera:", brojacd)
#printam rezultat
print("Tvoja ruka:\n",ruka)
print("Ruka dealera:\n", rukad)
if brojac>brojacd or brojacd>21:
      print("dobio si")
elif brojac==brojacd:
      print("nicija")
else:
      print("izgubio si")



            

