def havelHakimi(G):
    G=sorted(G,reverse=True)
    print(G)
    if G[0]<=(len(G)-1) and sum(G)%2==0 and sum(G)<= len(G)*(len(G)-1):
        while G[0]!=0:
            x=G[0]
            G[0]=0
            for i in range(1,x+1):
                G[i]=G[i]-1
            G=sorted(G,reverse=True)
            print(G)
    if sum(G)==0:
        result="Algorytm Havela Hakimiego: Ciąg wierzchołków jest graficzny"
    else:
        result="Algorytm Havela Hakimiego: Ciąg wierzchołków nie jest graficzny"
    return result

def suma(S,j,k):
    s=0
    for i in range(j,k):
        s=s+S[i]
    return s

def suma_min(S,j,n):
    s=0
    for i in range(j,n):
        m=min(j,S[i])     
        s=s+m
    return s

def erdosGallai(G):
    G=sorted(G, reverse=True)
    n=len(G)
    X=[]
    if sum(G)%2==0:
        print("Ciag jest parzysty")
        for k in range(1,n):
            print(str(suma(G,0,k)) + "<=" +str(k*(k-1) + suma_min(G,k,n))+"?")
            if suma(G,0,k)<=k*(k-1) + suma_min(G,k,n):
                x=1
                X.append(x)
            else:
                x=0
                X.append(x)
    if sum(X)==len(G)-1:
        result="Algorytm Erdosa i Gallai: Ciąg wierzchołków jest graficzny"
    else:
        result="Algorytm Erdosa i Gallai: Ciąg wierzchołków nie jest graficzny"
    return result


# sprawdzanie na podstawie ciagu wierzcholkow ze zbioru zadan
print("3,3,2,2,2,2,1,1")
print(havelHakimi([3,3,2,2,2,2,1,1]))
print(erdosGallai([3,3,2,2,2,2,1,1]))
print("7,6,6,5,4,3,2,1")
print(havelHakimi([7,6,6,5,4,3,2,1]))
print(erdosGallai([7,6,6,5,4,3,2,1]))
print("5,5,5,4,4,3")
print(havelHakimi([5,5,5,4,4,3]))
print(erdosGallai([5,5,5,4,4,3]))
print("5,4,3,2,1")
print(havelHakimi([5,4,3,2,1]))
print(erdosGallai([5,4,3,2,1]))