sommets=[1,2,3,4,5,6,7]
arc=[[1,2],[1,3],[1,5],[2,3],[2,6],[2,7],[3,4],[3,7],[4,6],[5,4],[7,6]]
poid=[4,2,7,2,2,10,10,1,20,2,12]
def Ford(sommets,arc,poid):
    dic ={}
    for i in range(len(sommets)):
        if i==0:
            dic [sommets[i]]=0
        else:
            dic [sommets[i]]=100000000
    i=0
    while(i<len(sommets)):
        for  ac in range(len(arc)):
            if arc[ac][0]==sommets[i]:
                dest=arc[ac][1]
                if dic[dest]>dic[sommets[i]]+poid[ac]:
                    dic[dest]=dic[sommets[i]]+poid[ac]
                    if i>dest-1:
                        i=dest-1
                    
        i=i+1     
    print(dic)  
    return dic
            
Ford(sommets,arc,poid)
