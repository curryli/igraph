from igraph import *  
import re
import timeit

start = timeit.default_timer()

#graph = Graph.Read_Pickle("igraph.pickle")  
graph = Graph.Read_Pajek("gephi.net")
summary(graph)

##cores = Graph.coreness(graph)
##print type(cores)
##print cores

##subgraph = graph.k_core(10,20,30)
##print subgraph
##for i in subgraph:
##    plot(i)



coreness = graph.shell_index(mode=OUT)
coreness.sort(reverse = True)
for i in range(3):
    print coreness[i]

coreness = graph.shell_index(mode=IN)
print max(coreness)

coreness = graph.shell_index(mode=ALL)
print max(coreness)

k_list = range(3,11)
##subgraph = graph.k_core(k_list)
for i in k_list:
    subgraph = graph.k_core(i)
    subgraph.write_pajek("kcore" + str(i) + ".net")


    
stop = timeit.default_timer()
print("Time Used :" ,(stop-start))
