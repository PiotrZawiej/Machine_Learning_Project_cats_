import random

class Kot:
    def __init__(self):
            self.zdobyte_punkty = 0
            self.lista_posiadanych_chunkow = []  # Initialize the list in __init__
            self.lista_chunkow_do_wyboru = []

    




tablica_obiektow = []
k=0
tablesize=5000
chunksize=2500

'''
Luna = mysze = "M" = 1
Dante = kamyki i liscie= "K" = 2
Ariana = slimaki = "S" = 3
'''
tablica_obiektow.append([1,1,"K"])

tablica_obiektow.append([2000,3000,"S"])

tablica_obiektow.append([3000,2000,"S"])

tablica_obiektow.append([5000,5000,"K"])
tablica_obiektow.append([5000,5000,"K"])
tablica_obiektow.append([5000,5000,"K"])
tablica_obiektow.append([5000,5000,"K"])

tablica_obiektow.append([5000,5000,"M"])
tablica_obiektow.append([5000,5000,"M"])
tablica_obiektow.append([5000,5000,"M"])
tablica_obiektow.append([5000,5000,"M"])
tablica_obiektow.append([5000,5000,"M"])
tablica_obiektow.append([5000,5000,"M"])

#tworzenie tablicy z losowymi obiektami w losowych punktach 5000x5000 + obiekt ktory tam sie znajduje
for i in range(k):
    obiekt=""
    match random.randint(1,3):
        case 1:
            obiekt = "M"
        case 2:
            obiekt = "K"
        case 3:
            obiekt = "S"

    tablica_obiektow.append([random.randint(0, tablesize),random.randint(0, tablesize), obiekt ] )

                   

#dzielenie tablicy glownej na mniejsze kwadraty, chunk
tablica_chunkow = []

for y in range(int(tablesize/chunksize)):
    for x in range(int(tablesize/chunksize)):

        M=0
        K=0
        S=0
        do_usuniecia =[]
        for i in range( len(tablica_obiektow)):
            if( (tablica_obiektow[i][0]>= x*chunksize and tablica_obiektow[i][0]<= (x+1)*chunksize) and (tablica_obiektow[i][1]>= y*chunksize and tablica_obiektow[i][1]<= (y+1)*chunksize) ):
                match tablica_obiektow[i][2]:
                    case "M":
                        M+=1
                    case "K":
                        K+=1
                    case "S":
                        S=1
                do_usuniecia.append(i)
        
        for i in range(len(do_usuniecia)-i):
            del tablica_obiektow[do_usuniecia[i]]

        tablica_chunkow.append([M,K,S])

#print(tablica_chunkow)
'''
-=inicjalizacja kotow + koty wybieraja najlepsza pozycje startowa=-
'''
Luna=Kot()
Dante=Kot()
Ariana= Kot()
tablica_kotow =[Luna,Dante,Ariana]

'''
-=algorytm sprawdzania dostepnych kratek + przypisanie kratki kotu=-
'''
#wybur chunka dla kazdego kota bez powturzen

top_3_values = []
for i in range(len(tablica_chunkow[0])):
    # Sort the list_of_lists based on the values at the current index
    sorted_lists = sorted(enumerate(tablica_chunkow), key=lambda x: x[1][i], reverse=True)

    # Extract the 3 biggest values and their indexes
    top_3_values.append([(value[i], index) for index, value in sorted_lists[:3]]) 

offset_pozycji=[0,0,0]
for i in range(len(tablica_kotow)):
    for j in range(len(tablica_kotow)):

        #jezeli indeksy maja konflikty
        if j!= i and top_3_values[i][offset_pozycji[i]][1] == top_3_values[j][offset_pozycji[j]][1] :
            
            #mniejsza wartosc pod indeksem dostaje offset
            if top_3_values[i][offset_pozycji[i]][0] >= top_3_values[j][offset_pozycji[j]][0]:
                offset_pozycji[j]+=1
            else:
                offset_pozycji[i]+=1

#wpisanie chunka startowego
for i in range(len(tablica_kotow)):
    tmp = top_3_values[i][offset_pozycji[i]][1]
    tablica_kotow[i].lista_posiadanych_chunkow.append(tmp)




#przypisywanie kolejnych chunkow
keep_looping=True
#while(keep_looping):

    



