import networkx as nx
import matplotlib.pyplot as plt
P1EXIM = nx.DiGraph()
P1EXIM.add_node("Germany")
P1EXIM.add_node("Finland")
P1EXIM.add_node("Sweden")
P1EXIM.add_node("Denmark")
P1EXIM.add_node("Norway")
P1EXIM.add_node("Iceland")
P1EXIM.add_node("China")
P1EXIM.add_node("Netherlands")
P1EXIM.add_node("United States")
P1EXIM.add_node("United Kingdom")
P1EXIM.add_node("Spain")
P1EXIM.add_node("France")



#Export
P1EXIM.add_edge("Germany", "Finland", weight=0.5)
P1EXIM.add_edge("Sweden", "Finland", weight=0.5)
P1EXIM.add_edge("China", "Finland", weight=0.5)
P1EXIM.add_edge("Netherlands", "Finland", weight=0.5)
P1EXIM.add_edge("United States", "Finland", weight=0.5)
P1EXIM.add_edge("Norway", "Sweden", weight=0.5)
P1EXIM.add_edge("Germany", "Sweden", weight=0.5)
P1EXIM.add_edge("Denmark", "Sweden", weight=0.5)
P1EXIM.add_edge("United States", "Sweden", weight=0.5)
P1EXIM.add_edge("Finland", "Sweden", weight=0.5)
P1EXIM.add_edge("Sweden", "Norway", weight=0.5)
P1EXIM.add_edge("Germany", "Norway", weight=0.5)
P1EXIM.add_edge("United Kingdom", "Norway", weight=0.5)
P1EXIM.add_edge("Netherlands", "Norway", weight=0.5)
P1EXIM.add_edge("France", "Norway", weight=0.5)
P1EXIM.add_edge("United Kingdom", "Iceland", weight=0.5)
P1EXIM.add_edge("Netherlands", "Iceland", weight=0.5)
P1EXIM.add_edge("Germany", "Iceland", weight=0.5)
P1EXIM.add_edge("Spain", "Iceland", weight=0.5)
P1EXIM.add_edge("United States", "Iceland", weight=0.5)
P1EXIM.add_edge("United Kingdom", "Denmark", weight=0.5)
P1EXIM.add_edge("Sweden", "Denmark", weight=0.5)
P1EXIM.add_edge("Germany", "Denmark", weight=0.5)
P1EXIM.add_edge("United States", "Denmark", weight=0.5)
P1EXIM.add_edge("Norway", "Denmark", weight=0.5)




in_degrees = P1EXIM.in_degree("Finland")  + P1EXIM.in_degree("Norway") + P1EXIM.in_degree("Denmark") + P1EXIM.in_degree("Iceland") + P1EXIM.in_degree("Sweden")
in_degrees1 = in_degrees/5
print("The average in_degree of nordic countries is", in_degrees1)

out_degrees = P1EXIM.out_degree("Finland")  + P1EXIM.out_degree("Norway") + P1EXIM.out_degree("Denmark") + P1EXIM.out_degree("Iceland") + P1EXIM.out_degree("Sweden")
out_degrees1 = out_degrees/5
print("The average out_degree of nordic countries is", out_degrees1)
nx.draw(P1EXIM,with_labels=True,edge_color="red")

avgclustering = (nx.clustering(P1EXIM,"Finland") + nx.clustering(P1EXIM,"Sweden") + nx.clustering(P1EXIM,"Denmark") + nx.clustering(P1EXIM,"Iceland") + nx.clustering(P1EXIM,"Norway"))/5
print("The average clustering coefficient for nordic countries is ", avgclustering)

shortest_paths = dict(nx.shortest_path_length(P1EXIM))
shortest_paths = {"Finland": {"Finland": 0, "France": 3, "Sweden": 1, "China": 1, "Denmark": 2, "Norway": 2, "Germany": 1, "Netherlands": 1, "United States": 1, "United Kingdom": 2, "Iceland": 2, "Spain": 3},
"Sweden": {"Sweden": 0, "Finland": 1, "Denmark": 1, "Norway": 1, "China": 2, "France": 2, "Germany": 1, "Netherlands": 1, "United States": 1, "Iceland": 2, "United Kingdom": 1, "Spain": 3},
"Iceland": {"Iceland": 0, "Spain": 1, "United Kingdom": 1, "United States": 1, "Netherlands": 1, "Germany": 1, "Norway": 1, "Sweden": 2, "Denmark": 2, "Finland": 2, "China": 2, "France": 1},
"Denmark": {"Denmark": 0, "Sweden": 1, "Finland": 2, "China": 1, "Norway": 1, "Germany": 1, "Netherlands": 1, "United Kingdom": 1, "United States": 1, "France": 2, "Iceland": 2, "Spain": 3},
"Norway": {"Denmark": 1, "Norway": 0, "Sweden": 1, "Germany": 1, "Netherlands": 1, "China": 1, "Finland": 2, "France": 1, "United States": 1, "United Kingdom": 1, "Iceland": 1, "Spain": 2}}

node_path_avg = [sum(paths.values()) / len(P1EXIM.nodes) for node, paths in shortest_paths.items()]

print("The path lengths average for each nordic country (Finland, Sweden, Iceland, Denmark, Norway) is", node_path_avg)

plt.show()


