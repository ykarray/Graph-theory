sommets=[1,2,3,4,5,6,7]
arc=[[1,2],[1,3],[1,5],[2,3],[2,6],[2,7],[3,4],[3,7],[4,6],[5,4],[7,6]]
poid=[4,2,7,2,2,10,10,1,20,2,12]
def pred(sommets,arc,poid):
    pred={}
    for i in sommets:
        pred[i]=[]
    for i in range(len(arc)):
        pred[arc[i][1]].append(arc[i][0])
    return pred
def ordonnancement(sommets,arc,poid):
    prede = pred(sommets,arc,poid)
    niv={}
    som_in_niv=[]
    n=1
    while(len(som_in_niv)<len(sommets)):
        for i in prede.keys():
            for j in prede[i]:
                if j in som_in_niv:
                    prede[i].remove(j)
        niv[n]=[]
        for i in prede.keys():
            if (prede[i]==[])and(i not in som_in_niv ):
                niv[n].append(i)
                som_in_niv.append(i)
        if niv[n]!=[]:
            n=n+1
        
    
    return niv
def bellman(sommets,arc,poid,src):
    niv=ordonnancement(sommets,arc,poid)
    prede = pred(sommets,arc,poid)
    s=[src]
    p={}
    for i in range(len(sommets)):
        if sommets[i]==src:
            p[src]=0
        else:
            p[sommets[i]]=100000000
    h=list(niv.keys())   
    for i in range(2,len(h)+1,1):
        niv_bef=[]
        for k in range(1,i,1):
            niv_bef.extend(niv[k])
        for j in niv[i]:
            mi=100000
            for h in prede[j]:
                if (h in niv_bef)and (mi>p[h]+poid[arc.index([h,j])]):
                    mi=p[h]+poid[arc.index([h,j])]
                    
                p[j]=min(p[j],mi)
                s.append(j)
        print(p)
    return p
bellman(sommets,arc,poid,1)

