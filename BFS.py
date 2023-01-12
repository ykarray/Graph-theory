def bfs(g,s,nbs):
    i=0
    
    som=[s]
    arete=[]
    s=g.keys()
    while (len(som)< nbs):
        
        for so in g[som[i]]:
            if so not in som :
                arete.append([som[i],so])
                som.append(so)
        i=i+1
        while((som[i] not in s )and(len(som)<nbs)):
              i=i+1
    
    print(som)
 
    
    


    
