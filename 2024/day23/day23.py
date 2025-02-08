import networkx as nx

with open("input.txt", "r") as f:
    input = f.readlines()


graph = nx.Graph()


for line in input:
    computer_1, computer_2 = line.strip().split("-")
    graph.add_edge(computer_1, computer_2)


cliques = list(nx.find_cliques(graph))

largest_clique = max(cliques, key=len)

print(",".join(sorted(largest_clique)))
