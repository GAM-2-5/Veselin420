import random
ruka=""    
brojac=0
novac=1000
def gubitak():
      if novac<=0:
            print("Potrošio si sav svoj novac!!!")
            quit("Potrošio si sav novac!!!")
      elif novac>999999:
            print("Svaka čast, prešao si igru osvojivši jedan milijun!!!")
      else:
            print("Imaš ", novac, " kuna")
            start=input().lower()
            if start==("start"):
                  main()
            else:
                  quit()

def main():
      global novac
      global ruka
      global brojac
      f = open("cards.txt", "r")
      karte=[]
      ruka=""
      rukad=""
      brojac=0
      brojacd=0
      indikator=0
      indikatord=0
      komanda="hit"
      print("Imaš ", novac, " kuna")
      ulog=int(input("\nKoliko želiš uložiti?\n"))
      for x in f:
            karte.append(x)
            
      def uzimanje():
            global ruka
            global brojac
            global novac
            karta=karte[random.randint(0,50)]
            while ruka.count(karta)==1 or rukad.count(karta)==1: 
                  karta=karte[random.randint(0,50)]
            ruka+=karta
            if karta[0].isdigit(): 
                  brojac+=int(karta[0])
            elif karta[0]=="t"or"k"or"j"or"q":
                  brojac+=10
            elif karta[0]=="a":
                  brojac+=11
            elif brojac>21 and ruka.count("Ace")!=0 and indikator==0 :
                  brojac=brojac-ruka.count("Ace")*10
                  indikator+=1
            if brojac>21:
                  print("Ruka dealera:\n",rukad)
                  print("Tvoja ruka:\n",ruka)
                  novac-=ulog
                  print ("Izgubio si!\nUpiši start za još jedan pokušaj")
                  gubitak()
      
      kartad=karte[random.randint(0,50)]
      while ruka.count(kartad)==1 or rukad.count(kartad)==1: 
            kartad=karte[random.randint(0,50)]
      rukad+=kartad
      if kartad[0].isdigit():
            brojacd+=int(kartad[0])
      elif kartad[0]=="t"or"k"or"j"or"q":
            brojacd+=10
      elif kartad[0]=="a" and brojacd+11>21:
            brojacd+=1
      elif kartad[0]=="a":
            brojacd+=11
      if ulog>novac:
            ulog=novac
      uzimanje()
      while (komanda=="hit"):
            uzimanje()
            print("Ruka dealera:\n",rukad)
            print("Tvoja ruka:\n",ruka)
            komanda=input("Hit or stand?\n").lower()

      while brojacd<brojac:
            kartad=karte[random.randint(0,50)]
            while ruka.count(kartad)==1 or rukad.count(kartad)==1: 
                  kartad=karte[random.randint(0,50)]
            rukad+=kartad
            if kartad[0].isdigit():
                  brojacd+=int(kartad[0])
            elif kartad[0]=="t"or"k"or"j"or"q":
                  brojacd+=10
            elif brojacd>21 and rukad.count("Ace")!=0 and indikatord==0 :
                  brojacd=brojacd-rukad.count("Ace")*10
                  indikatord+=1
            elif kartad[0]=="a":
                  brojacd+=11
      print("Tvoja ruka:\n",ruka)
      print("Ruka dealera:\n", rukad)
      if brojac>brojacd or brojacd>21:
            print ("Dobio si!\nUpiši start za još jednu igru")
            novac+=ulog
            gubitak()
      elif brojac==brojacd:
            print ("Ničija je!\nUpiši start za još jedan pokušaj")
            gubitak()
      else:
            print ("Izgubio si!\nUpiši start za još jedan pokušaj")
            novac-=ulog
            gubitak()
main()

            

