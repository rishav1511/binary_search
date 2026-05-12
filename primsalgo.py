import sys
def minkey(key,mstSet,n):
    min_value=sys.maxsize
    min_index=-1
    for v in range(n):
        if mstSet[v]==False and key[v]<min_value:
            min_value=key[v]
            min_index=v
    return min_index
def printMST(parent,c,n):
    totalweight=0
    print("Edge \t Weight ")
    for i in range(1,n):
        print(parent[i]+1,"-",i+1,"\t",c[i][parent[i]])
        totalweight+=c[i][parent[i]]
    print("Total cost for the minimum spanning tree= ",totalweight)
def primMST(c,n):
    parent=[None]*n
    key=[sys.maxsize]*n
    mstSet=[False]*n
    key[0]=0
    parent[0]=-1
    for _ in range(n-1):
        u=minkey(key,mstSet,n)
        mstSet[u]=True
        for v in range(n):
            if c[u][v] > 0 and mstSet[v] == False and c[u][v] < key[v]:
                key[v]=c[u][v]
                parent[v]=u
    printMST(parent,c,n)
n=int(input("Enetr no of vertex: "))
c=[]
print("Enter the cost adjacency matrix: ")
for i in range(n):
    c.append(list(map(int,input().split())))
primMST(c,n)

