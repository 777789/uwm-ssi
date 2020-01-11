openFileSys = open('data/car.txt')
try:
    sysDec = openFileSys.read() 
finally:
    openFileSys.close()
  
openFileType = open('data/car-type.txt')
try: 
    sysType = openFileType.read()
finally:
    openFileType.close()

openFileDis = open('data/_info-data-discrete.txt')
try: 
    sysDisc = openFileDis.read()  
finally:
    openFileDis.close()

sysD = 'car'

tab = []
sys = []
allSysDec = []
tabTemp = []
num = []
num2 = []
dec = []
decInt = [
        0, 0, 0, 0
]
x = 0
average = 0
variance = 0


sys = sysDisc.split("\n")
for line in sys:
    tab = line.split(" ")
    if(tab[0] == sysD):
        tab = line.split(" ")
        numberOfAttributes = int(tab[1]) - 1
        numberOfObjects = tab[2]
    
    
sys = sysDec.split("\n")
for line in sys:
    a = line.split(" ,")
    for lin in a:
        b = lin.split(" ")
        if(b != ['']):
            allSysDec.append(b[numberOfAttributes])


def funkcja(kolumna):
    for line in sys:
        a = line.split(",")
        for lin in a:
            b = lin.split(" ")
            if(b != ['']):
                num.append(b[kolumna])

                
def funkcja2(kolumna):
    for line in sys:
        a = line.split(" ,")
        for lin in a:
            b = lin.split(" ")
            if(b != ['']):
                tabTemp.append(b[kolumna])


dec = list(set(allSysDec))
print("1. Klasy decyzyjne: " + str(dec))

print("2. Wielkosci klas decyzyjnych:")
for i in range(0, len(dec)):
    for j in allSysDec:
        if(j == dec[i]):
            decInt[i] += 1;
for z in range(len(dec)):
    print(dec[z] + " " + str(decInt[z]))

print("3. Minimalne i maksymalne wartości poszczególnych atrybutów:")
typee = sysType.split("\n")
for line in typee:
    a = line.split(" ")
    x=x + 1
    if(a[1] == 'n'):
        funkcja(x - 1)
        try:
            if((int(min(num)))):
                print("Atrybut:" + str(x) + " min: " + str(min(num)))
        except ValueError:
            print("Atrybut:" + str(x) + " min nie jest liczba")
        try:
            if((int(max(num)))):
                 print("Atrybut:" + str(x) +" max: " + str(max(num)))
        except ValueError:
            print("Atrybut:" + str(x) + " max nie jest liczbą")
    else:
        print("Atrybut:" + str(x) + " nie jest atrybutem numerycznym")

print("4. Dla każdego atrybutu liczba różnych dostępnych wartości:")
for i in range(0, numberOfAttributes+1):
    funkcja2(i) 
    print("Atrybut " + str(i + 1) + ":")
    print(len(list(set(tabTemp))))
    tabTemp.clear()                   
                
print("5. Dla każdego atrybutu wypisujemy listę wszystkich" 
      "różnych dostępnych wartości:")
for i in range(0, numberOfAttributes+1):
    funkcja2(i)
    print("Atrybut " + str(i + 1) + ":")
    print(list(set(tabTemp)))
    tabTemp.clear()

print("6. Odchylenie standardowe dla poszczególnych" 
      "atrybutów w całym systemie i w klasach decyzyjnych:")
x=0   
typee = sysType.split("\n")
for line in typee:
    a = line.split(" ")
    x=x + 1
    if(a[1] == 'n'):
        funkcja(x - 1)
        try:
            for liczba in num:
                average += liczba
            average = average / numberOfObjects
            for liczba in num:
                variance += ((liczba-average)**2) / (numberOfObjects)
            print("Warianca wynosi: " + sum(variance))
        except:
            print("Atrybut:" + str(x) +
                  " w zbiorze występują inne wartosci niż liczby")  
    else:
        print("Atrybut:" + str(x) + " nie jest atrybutem numerycznym")