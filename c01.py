import math


open_file_sys = open('data/car.txt')
try:
    sys_dec = open_file_sys.read() 
finally:
    open_file_sys.close()
  
open_file_type = open('data/car-type.txt')
try: 
    sys_type = open_file_type.read()
finally:
    open_file_type.close()

open_file_dis = open('data/_info-data-discrete.txt')
try: 
    sys_disc = open_file_dis.read()  
finally:
    open_file_dis.close()

sys_d = 'car'

tab = []
sys = []
all_sys_dec = []
tab_temp = []
num = []
num_2 = []
dec = []
dec_int = [
        0, 0, 0, 0
]
x = 0
average = 0
variance = 0


sys = sys_disc.split("\n")
for line in sys:
    tab = line.split(" ")
    if(tab[0] == sys_d):
        tab = line.split(" ")
        number_of_attributes = int(tab[1]) - 1
        number_of_objects = tab[2]
    
    
sys = sys_dec.split("\n")
for line in sys:
    a = line.split(" ,")
    for lin in a:
        b = lin.split(" ")
        if(b != ['']):
            all_sys_dec.append(b[number_of_attributes])


def function(column):
    for line in sys:
        a = line.split(",")
        for lin in a:
            b = lin.split(" ")
            if(b != ['']):
                num.append(b[column])

                
def function_2(column):
    for line in sys:
        a = line.split(" ,")
        for lin in a:
            b = lin.split(" ")
            if(b != ['']):
                tab_temp.append(b[column])


dec = list(set(all_sys_dec))
print("1. Klasy decyzyjne: " + str(dec))

print("2. Wielkosci klas decyzyjnych:")
for i in range(0, len(dec)):
    for j in all_sys_dec:
        if(j == dec[i]):
            dec_int[i] += 1;
for z in range(len(dec)):
    print(dec[z] + " " + str(dec_int[z]))

print("3. Minimalne i maksymalne wartości poszczególnych atrybutów:")
typee = sys_type.split("\n")
for line in typee:
    a = line.split(" ")
    x=x + 1
    if(a[1] == 'n'):
        function(x - 1)
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
for i in range(0, number_of_attributes+1):
    function_2(i) 
    print("Atrybut " + str(i + 1) + ":")
    print(len(list(set(tab_temp))))
    tab_temp.clear()                   
                
print("5. Dla każdego atrybutu wypisujemy listę wszystkich " 
      "różnych dostępnych wartości:")
for i in range(0, number_of_attributes+1):
    function_2(i)
    print("Atrybut " + str(i + 1) + ":")
    print(list(set(tab_temp)))
    tab_temp.clear()

print("6. Odchylenie standardowe dla poszczególnych" 
      "atrybutów w całym systemie i w klasach decyzyjnych:")
x=0   
typee = sys_type.split("\n")
for line in typee:
    a = line.split(" ")
    x=x + 1
    if(a[1] == 'n'):
        function(x - 1)
        try:
            for number in num:
                average += number
            average = average / number_of_objects
            for number in num:
                variance += ((number-average)**2) / (number_of_objects)
            standard_deviation = math.sqrt(sum(variance))
            print("Odchylenie standardowe wynosi: " 
                  + str(standard_deviation))
        except:
            print("Atrybut:" + str(x) +
                  " w zbiorze występują inne wartosci niż liczby")  
    else:
        print("Atrybut:" + str(x) + " nie jest atrybutem numerycznym")