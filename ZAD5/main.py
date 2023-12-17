import random

class Kot:
    index_preferowanego_biektu = -1
    zdobyte_punkty=0
    lista_posiadanych_chunkow=[]
    lista_chunkow_do_wyboru=[]




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
tablica_obiektow.append([5000,5000,"K"])
tablica_obiektow.append([5000,5000,"K"])
tablica_obiektow.append([5000,5000,"K"])
tablica_obiektow.append([5000,5000,"K"])
tablica_obiektow.append([5000,5000,"K"])

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

for x in range(int(tablesize/chunksize)):
    for y in range(int(tablesize/chunksize)):

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


'''
-=inicjalizacja kotow + koty wybieraja najlepsza pozycje startowa=-
'''
Luna=Kot
Dante=Kot
Ariana= Kot
Luna.index_preferowanego_biektu=1
Dante.index_preferowanego_biektu =2
Ariana.index_preferowanego_biektu=3
    
tablica_kotow =[Luna,Dante,Ariana]

print(tablica_chunkow)

'''
-=algorytm sprawdzania dostepnych kratek + przypisanie kratki kotu=-
'''