from igraph import *  
import re
import timeit

start = timeit.default_timer()

N=55455
graph = Graph.Read_Pajek("gephiByname.net")
graph.vs["name"] = range(0,N)
summary(graph) 
k_list = range(10,11)

for i in k_list:
    subgraph = graph.k_core(i)
    vertices = subgraph.vs["name"]
    #edgelist = subgraph.get_edgelist()
    print vertices
    #subgraph.write_pajek("kcoreLabel" + str(i) + ".net")
    subgraph.write_graphml("kcoreLabel" + str(i) + ".graphml")

    
stop = timeit.default_timer()
print("Time Used :" ,(stop-start))
