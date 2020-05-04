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
P1.add_node("United Kingdom")
P1.add_node("United States")
P1.add_node("South Korea")
P1.add_node("France")
P1.add_edge("France", "Iceland")
P1.add_edge("Germany", "Iceland")
P1.add_edge("United Kingdom", "Iceland")
P1.add_edge("Netherlands", "Iceland")
P1.add_edge("Norway", "Iceland")
P1.add_edge("Sweden", "Norway")
P1.add_edge("Germany", "Norway")
P1.add_edge("China", "Norway")
P1.add_edge("South Korea", "Norway")
P1.add_edge("United States", "Norway")
P1.add_edge("Germany", "Sweden")
P1.add_edge("Denmark", "Sweden")
P1.add_edge("Netherlands", "Sweden")
P1.add_edge("Norway", "Sweden")
P1.add_edge("United Kingdom", "Sweden")
P1.add_edge("Germany", "Finland")
P1.add_edge("China", "Finland")
P1.add_edge("Sweden", "Finland")
P1.add_edge("Netherlands", "Finland")
P1.add_edge("Russia", "Finland")
P1.add_edge("Germany", "Denmark")
P1.add_edge("Sweden", "Denmark")
P1.add_edge("China", "Denmark")
P1.add_edge("Norway", "Denmark")
P1.add_edge("Netherlands", "Denmark")

in_degrees = P1.in_degree("Finland")  + P1.in_degree("Norway") + P1.in_degree("Denmark") + P1.in_degree("Iceland") + P1.in_degree("Sweden")
in_degrees1 = in_degrees/5
print("The average in_degree of nordic countries is", in_degrees1)

out_degrees = P1.out_degree("Finland")  + P1.out_degree("Norway") + P1.out_degree("Denmark") + P1.out_degree("Iceland") + P1.out_degree("Sweden")
out_degrees1 = out_degrees/5
print("The average out_degree of nordic countries is", out_degrees1)

avgclustering = (nx.clustering(P1,"Finland") + nx.clustering(P1,"Sweden") + nx.clustering(P1,"Denmark") + nx.clustering(P1,"Iceland") + nx.clustering(P1,"Norway"))/5
print("The average clustering coefficient for nordic countries is ", avgclustering)





nx.draw(P1,with_labels=True)
plt.show()