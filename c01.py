# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 08:08:26 2020

@author: Moj Komputer
"""

# =============================================================================
# data/car.txt
# data/car-type.txt
# data/_info-data-discreate.txt
# =============================================================================

OpenFileSys = open('data/car.txt')
try:
    SysDec = OpenFileSys.read() 
finally:
    OpenFileSys.close()
#    
OpenFileType = open('data/car-type.txt')
try: 
    SysType = OpenFileType.read()  
finally:
    OpenFileType.close()
#
OpenFileType = open('data/_info-data-discrete.txt')
try: 
    SysDisc = OpenFileType.read()  
finally:
    OpenFileType.close()
#
SysD = 'car'

tab = []
Sys = []
AllSysDec = []
TabTemp = []
Num = []
Num2 = []
Dec = []
DecInt = [0,0,0,0]
x = 0
Average = 0
Variance = 0

Sys = SysDisc.split("\n")
for line in Sys:
    tab = line.split(" ")
    if(tab[0]==SysD):
        tab = line.split(" ")
        NumberOfAttributes = int(tab[1]) - 1
        NumberOfObjects = tab[2]
    
    
Sys = SysDec.split("\n")
for line in Sys:
    a = line.split(" ,")
    for lin in a:
        b = lin.split(" ")
        if(b != ['']):
            AllSysDec.append(b[NumberOfAttributes])

def funkcja(kolumna):
    for line in Sys:
        a = line.split(",")
        for lin in a:
            b = lin.split(" ")
            if(b != ['']):
                Num.append(b[kolumna])
                
def funkcja2(kolumna):
    for line in Sys:
        a = line.split(" ,")
        for lin in a:
            b = lin.split(" ")
            if(b != ['']):
                TabTemp.append(b[kolumna])

Dec = list(set(AllSysDec)) #list tworzy liste a set unikalne i uporzadkowana kolekcja
print("1. Klasy decyzyjne: ")
print(str(Dec))
#
for i in range(0, len(Dec)):
    for j in AllSysDec:
        if(j==Dec[i]):
            DecInt[i]+=1;
print("2. Wielkosci klas decyzyjnych:")
for z in range(len(Dec)):
    print(Dec[z]+" "+str(DecInt[z]))

print("3. Minimalne i maksymalne wartości poszczególnych atrybutów")
Type = SysType.split("\n")
for line in Type:
    a = line.split(" ")
    x=x+1
    if(a[1]=='n'):
        funkcja(x-1)
        try:
            if((int(min(Num)))):
                print("Atrybut:" + str(x) +" min: " + str(min(Num)))
        except ValueError:
            print("Atrybut:" + str(x) + " min nie jest liczba")
        try:
            if((int(max(Num)))):
                 print("Atrybut:" + str(x) +" max: " + str(max(Num)))
        except ValueError:
            print("Atrybut:" + str(x) + " max nie jest liczbą")
    else:
        print("Atrybut:" + str(x) + " nie jest atrybutem numerycznym")

print("4. Dla każdego atrybutu liczba różnych dostępnych wartości")
for i in range(0, NumberOfAttributes+1):
    funkcja2(i) 
    print("Atrybut " + str(i+1) + ":")
    print(len(list(set(TabTemp))))
    TabTemp.clear()                   
                
print("5. Dla każdego atrybutu wypisujemy listę wszystkich różnych dostępnych wartości")
for i in range(0, NumberOfAttributes+1):
    funkcja2(i)
    print("Atrybut " + str(i+1) + ":")
    print(list(set(TabTemp)))
    TabTemp.clear()

print("6. Odchylenie standardowe dla poszczególnych atrybutów w całym systemie i w klasach decyzyjnych")
x=0   
Type = SysType.split("\n")
for line in Type:
    a = line.split(" ")
    x=x+1
    if(a[1]=='n'):
        funkcja(x-1)
        try:
            for liczba in Num:
                Average += liczba
            Average = Average/NumberOfObjects
            for liczba in Num:
                Variance += ((liczba-Average)**2)/(NumberOfObjects)
            print("Warianca wynosi: " + sum(Variance))
        except:
            print("Atrybut:"+str(x)+" w zbiorze występują inne wartosci niż liczby")
    
    else:
        print("Atrybut:" + str(x) + " nie jest atrybutem numerycznym")