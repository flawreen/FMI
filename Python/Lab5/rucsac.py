G = 8
ob = [(4, 8), (8, 12), (3, 6), (10,10)]
ob.sort(key=lambda x: x[1]/x[0], reverse=True)
print(ob)

def greedy(G, valori):
    sol = []
    suma = 0
    g = G
    total = sum(x[0] for x in valori)
    leng = len(valori)
    if total == G:
        for i in range(leng):
            sol.append(1)
        return sol, total
    for i in range(leng):
        if valori[i][0] <= g:
            sol.append(1)
            g -= valori[i][0]
            suma += valori[i][1]
        else:
            sol.append(g/valori[i][0])
            sol.extend([0 for i in range(i+1, leng)])
            suma += sol[i]*valori[i][1]
            return sol, suma
print(greedy(G, ob))