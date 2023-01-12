
def dfs(sommets_visite, graphe, s):  
    if s not in sommets_visite:
        print (s)
        sommets_visite.append(s)
        for v in graphe[s]:
            dfs(sommets_visite, graphe, v)


