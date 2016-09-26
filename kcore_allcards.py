from igraph import *  
import re
import timeit

start = timeit.default_timer()

N=55455
graph = Graph.Read_Pajek("gephiByname.net")
graph.vs["name"] = range(0,N)
summary(graph)

allcards = set()
k_list = range(7,11)
for i in k_list:
    subgraph = graph.k_core(i)
    vertices = set(subgraph.vs["name"])
    allcards |= vertices

with open("Kcards.txt","w") as FILEOUT:
    for card in allcards:
        print>>FILEOUT,card
 
    

 

    
stop = timeit.default_timer()
print("Time Used :" ,(stop-start))
