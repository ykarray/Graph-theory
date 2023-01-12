sommets=[1,2,3,4,5,6,7]
arc=[[1,2],[1,3],[1,5],[2,3],[2,6],[2,7],[3,4],[3,7],[4,6],[5,4],[7,6]]
poid=[4,2,7,2,2,10,10,1,20,2,12]
def dijkstra(sommets,arc,poid,src):
    chemin=[]
    k=[]
    l1=[]
    for i in range(len(sommets)):
        if sommets[i]==src:
            l1.append(0)
        else:
            l1.append(1000000000000)
    mat=[l1]
    print(l1,'\n')
    for i in range(len(sommets)-1):
        l=mat[i]
        min=1000000000000
        for j in mat[i]:
            if sommets[mat[i].index(j)] not in chemin:
                if j<min:
                    min=j
        
            
        index=mat[i].index(min)
        a=sommets[index]
        chemin.append(a)
        print('x',chemin[-1])
        for j in range(len(arc)):
            if arc[j][0]==a and poid[j]+mat[i][index]< l[arc[j][1]-1] :
                l[arc[j][1]-1]=poid[j]+mat[i][index]
                
        print(l,'\n')
        mat.append(l)
    
dijkstra(sommets,arc,poid,1)
    
