import igraph.test
from igraph import *  
g = Graph([(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)])
g.vs["name"] = ["Alice", "Bob", "Claire", "Dennis", "Esther", "Frank", "George"]
g.vs["age"] = [25, 31, 18, 47, 22, 23, 50]
g.vs["gender"] = ["f", "m", "f", "m", "f", "m", "m"]
g.es["is_formal"] = [False, False, True, True, True, False, True, False, False]

print g.es[0]
print g.es[0].attributes()
print g.degree()
print g.degree(6)
print g.degree([1,2,6])
print g.betweenness()
print g.edge_betweenness()
print g.pagerank()

ebs = g.edge_betweenness()
max_eb = max(ebs)
print [g.es[idx].tuple for idx, eb in enumerate(ebs) if eb == max_eb]

print g.vs.select(_degree = g.maxdegree())["name"]

layout = g.layout("kk")
##
##g.vs["label"] = g.vs["name"]
##color_dict = {"m": "blue", "f": "pink"}
##g.vs["color"] = [color_dict[gender] for gender in g.vs["gender"]]
##plot(g, layout = layout, bbox = (300, 300), margin = 20)

#layout = g.layout_kamada_kawai()
visual_style = {}
color_dict = {"m": "blue", "f": "pink"}
visual_style["vertex_size"] = 20
visual_style["vertex_label_dist"] = 1
visual_style["vertex_color"] = [color_dict[gender] for gender in g.vs["gender"]]
visual_style["vertex_label"] = g.vs["name"]
visual_style["edge_width"] = [1 + 2 * int(is_formal) for is_formal in g.es["is_formal"]]
visual_style["layout"] = layout
visual_style["bbox"] = (300, 300)
visual_style["margin"] = 30
plot(g, "social_network.pdf", **visual_style)


#plot(g) 
