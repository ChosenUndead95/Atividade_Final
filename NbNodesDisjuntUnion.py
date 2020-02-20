import queue
import networkx as nx
f = open("grafo.txt","r")
veta = []
vetb = []
vetc = []
for r in f:
    veta.append(r)
for r in veta[:-1]:
    vetb.append(r[:-1])
vetc.append(veta[-1].split())
veta = []
tamanho = 0
while True:
    veta.append(vetb[tamanho].split())
    if(vetb[tamanho] == vetb[-1]):
        break
    tamanho = tamanho+1
    
def totalNodes(adjac, n, x, y): 
       
    visited = [0] * (n + 1)  

    p = [None] * n 
  
    q = queue.Queue() 
    q.put(x)  
   
    visited[x] = True
  
    m = None
  
    while (not q.empty()): 
        m = q.get() 
        for i in range(len(adjac[m])): 
            h = adjac[m][i]  
            if (not visited[h]): 
                visited[h] = True 
                p[h] = m  
                q.put(h) 
    
    count = 0
   
    i = p[y]  
    while (i != x): 
        count += 1
        i = p[i] 
  
    return count 
  
if __name__ == '__main__': 
    adjac = [[] for k in range(tamanho+3)]  
    for a in range(tamanho + 1):
        adjac[int(veta[a][0])].append(int(veta[a][1]))
        adjac[int(veta[a][1])].append(int(veta[a][0]))  
  
    print(totalNodes(adjac, tamanho + 3, int(vetc[0][0]), int(vetc[0][1]))) 
