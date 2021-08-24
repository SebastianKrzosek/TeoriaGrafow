f = open("./dane.txt","r")  #czytamy dane o grafie z pliku tekstowego
l = f.readlines()           #graf zaczerpnałem prezentacji z wykładu
i = 0
edges = []

for linia in l: # w tym miejscu wycinam i zamieniam na inty dane z pliku
    linia = linia.strip()
    if i == 0:
        n = int(linia[0]) # wczytanie liczby wierzcholkow
        m = int(linia[2]) # wczytanie liczby krawedzi
    else:
        edges.append((int(linia[0]), int(linia[2]))) # wpisanie krawedzi do listy
    i = i + 1
print("")

print("Lista par")
for i, value in  enumerate(edges): # wypisanie danych pobranych wczesniej z pliku. Podane były tam w odpowiedniej formie
    print(value) 
print("")


print("Macierz sąsiedztwa")
matrix = [[0 for x in range(n)] for y in range(n)] # przy macierzy sasiedztwa wpisujemy 1 w wierzchołkach sasiednich
for edge in edges:    
    matrix[edge[0] - 1][edge[1] - 1] = 1
print("\t", end="")
for i in range(0, n):
    print(str(i + 1) + "\t", end='')
print("")

for x in range(0, n): #a nastepnie wypisujemy macierz z formatowaniem
    print(str(x + 1) + "\t",    end='')
    for y in range(0, n):
        print(matrix[x][y], end='')
        print("\t", end='')
    print("")
print("")


print("Macierz incydencji")
print("\t", end="")
for edge in edges:
    print("(" + str(edge[0]) + ", " + str(edge[1]) + ")\t", end='') #krawedzie
print("")
for x in range(0, n): #wypisanie odpowiednio 1 lub -1 zgodnie z kierunkiem krawedzi
    print(str(x + 1) + "\t", end='') 
    for y in range(0, m):
        if x + 1 == edges[y][0]: 
            print(-1, end='')
        elif x + 1 == edges[y][1]:
            print(1, end='')
        else:
            print(0, end='')
        print("\t", end='')
    print("")
print("")

print("Lista incydencji")

temp = 0
temp_count = 0
max_count = 0
count = 0
for edge in edges: #sprawdzanie wymiaru
    if max_count < count:
        max_count = count
    if(edge[0] == temp):
        count = count + 1
    else:
        temp = edge[0]
        count = 1

temp_matrix = [[0 for x in range(n)] for y in range(max_count)] #stworzenie macierzy o podanych wymiarach
temp = 0
col = 0
for edge in edges:
    if temp == edge[0]:
        col = col + 1
    else:
        col = 0
        temp = edge[0]
    temp_matrix[col][edge[0] - 1] = edge[1]

for x in range(0, n):
    print("[" + str(x  + 1) + "]\t", end='')
for x in range(0, max_count):
    print("")
    for y in range(0, n):
        if temp_matrix[x][y] == 0:
            print("\t", end='')
        else:
            print("[" + str(temp_matrix[x][y])+ "]\t", end='')
print("\n")

print("Dwie tablice")
naglowek = []
i = 0
temp = 0
for edge in edges:
    if temp != edge[0]:
        temp = edge[0]
        naglowek.append(i)
    i = i + 1

for x in range(0, n):
    print("[" + str(naglowek[x]) + "]\t", end='')  
print("")
for edge in edges:
    print("[" + str(edge[1]) + "]\t", end='')