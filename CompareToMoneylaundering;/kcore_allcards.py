from igraph import *  
import re
import timeit

start = timeit.default_timer()

N=55455
graph = Graph.Read_Pajek("gephi.net")
graph.vs["name"] = range(0,N)
summary(graph)

allcards = set()
k_list = range(8,11)
for i in k_list:
    subgraph = graph.k_core(i)
    subgraph.write_graphml("kcoreLabel" + str(i) + ".graphml")
    vertices = set(subgraph.vs["name"])
    allcards |= vertices

with open("Kcards.txt","w") as FILEOUT:
    for card in allcards:
        print>>FILEOUT,card
 
    

 

    
stop = timeit.default_timer()
print("Time Used :" ,(stop-start))
