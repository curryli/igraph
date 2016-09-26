from igraph import *  
import re
import timeit

start = timeit.default_timer()




g = Graph(directed=True)  # a directed graph

N=55455
for i in range(0,N):   
    g.add_vertex(i)
 
r = re.compile('\s+')
ff=open('Net.txt','r')
for line in ff.readlines():
    ItemList = r.split(line)
    ItemList[0]=int(ItemList[0])
    ItemList[1]=int(ItemList[1])
    g.add_edge(ItemList[0],ItemList[1])    
ff.close()

#g.write_gml("gephi.gml")
#g.write_graphml("gephi.graphml")
g.write_pajek("gephi.net")

stop = timeit.default_timer()
print("Done, Time Used :" ,(stop-start), " s.")
