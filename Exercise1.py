import networkx as nx
import matplotlib.pyplot as plt
P1 = nx.DiGraph()
P1.add_node("Germany")
P1.add_node("Finland")
P1.add_node("Sweden")
P1.add_node("Denmark")
P1.add_node("Norway")
P1.add_node("Iceland")
P1.add_node("China")
P1.add_node("Russia")
P1.add_node("Netherlands")
P1.add_node("United States")
P1.add_node("United Kingdom")
P1.add_node("Spain")
P1.add_edge("Germany", "Finland")
P1.add_edge("Sweden", "Finland")
P1.add_edge("China", "Finland")
P1.add_edge("Netherlands", "Finland")
P1.add_edge("Russia", "Finland")
P1.add_edge("Norway", "Sweden")
P1.add_edge("Germany", "Sweden")
P1.add_edge("Denmark", "Sweden")
P1.add_edge("United States", "Sweden")
P1.add_edge("Finland", "Sweden")
P1.add_edge("Sweden", "Norway")
P1.add_edge("Germany", "Norway")
P1.add_edge("United Kingdom", "Norway")
P1.add_edge("Netherlands", "Norway")
P1.add_edge("Denmark", "Norway")
P1.add_edge("United Kingdom", "Iceland")
P1.add_edge("Netherlands", "Iceland")
P1.add_edge("Germany", "Iceland")
P1.add_edge("Spain", "Iceland")
P1.add_edge("United States", "Iceland")
P1.add_edge("United Kingdom", "Denmark")
P1.add_edge("Sweden", "Denmark")
P1.add_edge("Germany", "Denmark")
P1.add_edge("China", "Denmark")
P1.add_edge("Netherlands", "Denmark")


in_degrees = P1.in_degree("Finland")  + P1.in_degree("Norway") + P1.in_degree("Denmark") + P1.in_degree("Iceland") + P1.in_degree("Sweden")
in_degrees1 = in_degrees/5
print("The average in_degree of nordic countries is", in_degrees1)

out_degrees = P1.out_degree("Finland")  + P1.out_degree("Norway") + P1.out_degree("Denmark") + P1.out_degree("Iceland") + P1.out_degree("Sweden")
out_degrees1 = out_degrees/5
print("The average out_degree of nordic countries is", out_degrees1)
nx.draw(P1,with_labels=True)

avgclustering = (nx.clustering(P1,"Finland") + nx.clustering(P1,"Sweden") + nx.clustering(P1,"Denmark") + nx.clustering(P1,"Iceland") + nx.clustering(P1,"Norway"))/5
print("The average clustering coefficient for nordic countries is ", avgclustering)

shortest_paths = dict(nx.shortest_path_length(P1))
shortest_paths = {"Finland": {"Finland": 0, "Russia": 1, "Sweden": 1, "China": 1, "Denmark": 2, "Norway": 2, "Germany": 1, "Netherlands": 1, "United States": 2, "United Kingdom": 3, "Iceland": 2, "Spain": 3},
"Sweden": {"Sweden": 0, "Finland": 1, "Denmark": 1, "Norway": 1, "China": 2, "Russia": 2, "Germany": 1, "Netherlands": 2, "United States": 1, "Iceland": 2, "United Kingdom": 2, "Spain": 3},
"Iceland": {"Iceland": 0, "Spain": 1, "United Kingdom": 1, "United States": 1, "Netherlands": 1, "Germany": 1, "Norway": 2, "Sweden": 2, "Denmark": 2, "Finland": 2, "China": 3, "Russia": 3},
"Denmark": {"Denmark": 0, "Sweden": 1, "Finland": 2, "China": 1, "Norway": 1, "Germany": 1, "Netherlands": 1, "United Kingdom": 1, "United States": 2, "Russia": 3, "Iceland": 2, "Spain": 3},
"Norway": {"Denmark": 1, "Norway": 0, "Sweden": 1, "Germany": 1, "Netherlands": 1, "China": 2, "Finland": 2, "Russia": 3, "United States": 2, "United Kingdom": 2, "Iceland": 3, "Spain": 4}}

node_path_avg = [sum(paths.values()) / len(P1.nodes) for node, paths in shortest_paths.items()]

print("The path lengths average for each nordic country (Finland, Sweden, Iceland, Denmark, Norway) is", node_path_avg)


plt.show()
