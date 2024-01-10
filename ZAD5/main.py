import random

class Kot:
    def __init__(self):
            self.zdobyte_punkty = 0
            self.lista_posiadanych_chunkow = []
            self.lista_chunkow_do_wyboru = []


tablica_obiektow = []
k=0
tablesize=5000
chunksize=1250
chunk_width=tablesize/chunksize

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
    top_3_values.append([(index,value[i] ) for index, value in sorted_lists[:3]]) 

offset_pozycji=[0,0,0]
for i in range(len(tablica_kotow)):
    for j in range(len(tablica_kotow)):

        #jezeli indeksy maja konflikty
        if j!= i and top_3_values[i][offset_pozycji[i]][0] == top_3_values[j][offset_pozycji[j]][0] :
            
            #mniejsza wartosc pod indeksem dostaje offset
            if top_3_values[i][offset_pozycji[i]][1] >= top_3_values[j][offset_pozycji[j]][1]:
                offset_pozycji[j]+=1
            else:
                offset_pozycji[i]+=1



#wpisanie chunka startowego + punkty
for i in range(len(tablica_kotow)):
    tablica_kotow[i].lista_posiadanych_chunkow.append(top_3_values[i][offset_pozycji[i]][0])
    tablica_kotow[i].zdobyte_punkty+= top_3_values[i][offset_pozycji[i]][1]


'''
-= przypisywanie kolejnych chunkow =-
'''
keep_looping=True
while(keep_looping):
    
    #keep_looping=False
    #znajdowanie sasiednich chunkow
    for i in tablica_kotow:
        for x in i.lista_posiadanych_chunkow:
            #chunk wyzej
            if x-chunk_width >= 0:
                i.lista_chunkow_do_wyboru.append(int(x-chunk_width))
            #chunk nizej
            if x+chunk_width <= chunk_width*chunk_width:
                i.lista_chunkow_do_wyboru.append(int(x+chunk_width))
            #chunk na lewo
            if  int((x-1) / chunk_width) == int(x / chunk_width) and x-1 >=0:
                i.lista_chunkow_do_wyboru.append(x-1)
            #chunk na prawo
            if  int((x+1) / chunk_width) == int(x / chunk_width) and x+1 <= (chunk_width*chunk_width)-1:
                i.lista_chunkow_do_wyboru.append(x+1)

        i.lista_chunkow_do_wyboru = list(set(i.lista_chunkow_do_wyboru))#pozbycie sie duplikatow
            
    #usuwanie chunkow posiadanych juz przez inne koty
    all_posiadane = set()
    for kot in tablica_kotow:
        all_posiadane.update(kot.lista_posiadanych_chunkow)

    # Remove integers from lista_chunkow_do_wyboru based on the set of all_posiadane
    for kot in tablica_kotow:
        kot.lista_chunkow_do_wyboru = [item for item in kot.lista_chunkow_do_wyboru if item not in all_posiadane]

    top_3_values.clear()
    liczba=0
    #top3
    for kot in tablica_kotow:

        for i in range(len(tablica_chunkow[0])):
            # Sort the list_of_lists based on the values at the current index
            sorted_lists = sorted(enumerate(tablica_chunkow), key=lambda x: x[1][i], reverse=True)

        # Filter out values where the index matches one of the numbers in the goodint list
        top_values_for_index = [(value, index[liczba]) for value, index in sorted_lists if value in kot.lista_chunkow_do_wyboru]
        liczba+=1
        # Add the kot_top_3_values to the main top_3_values list
        top_3_values.append(top_values_for_index[:3])



    # Ensure each sublist has exactly three elements by adding (-1, -1) for missing values
    top_3_values = [sublist + [(-1, -1)] * (3 - len(sublist)) for sublist in top_3_values]


    offset_pozycji=[0,0,0]
    #zwiekszanie offsetu aby nie wybierac tych samych indexow
    for i in range(len(tablica_kotow)):
        for j in range(len(tablica_kotow)):
            if top_3_values[i][offset_pozycji[i]][0] != -1 or top_3_values[j][offset_pozycji[j]][0] != -1:
                #jezeli indeksy maja konflikty
                if j!= i and top_3_values[i][offset_pozycji[i]][0] == top_3_values[j][offset_pozycji[j]][0] :
                    
                    #mniejsza wartosc pod indeksem dostaje offset
                    if top_3_values[i][offset_pozycji[i]][1] >= top_3_values[j][offset_pozycji[j]][1]:
                        offset_pozycji[j]+=1
                    else:
                        offset_pozycji[i]+=1

    #wpisanie kolejnego chunka + punkty
    for i in range(len(tablica_kotow)):
        tmp = top_3_values[i][offset_pozycji[i]][1]
        if tmp != -1:
            tablica_kotow[i].lista_posiadanych_chunkow.append(top_3_values[i][offset_pozycji[i]][0])
            tablica_kotow[i].zdobyte_punkty+= top_3_values[i][offset_pozycji[i]][1]

    #zakoncz przypisywani chunkow jak juz nie ma potecjalnych chunkow
    suma=0
    for i in range(len(top_3_values)):
        suma += top_3_values[i][0][0]

        



    if suma in [-2 ,-3]:
        keep_looping = False



for kot in tablica_kotow:
    print(kot.lista_posiadanych_chunkow)