#r: networkx
#r: matplotlib

import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore

#create a Graph
G = nx.Graph()

#add nodes
G.add_node('node1')
G.add_node('node2')
G.add_node('node3')
G.add_node('node4')
G.add_node('node5')
G.add_node('node6')
G.add_node('node7')


#add edges
G.add_edge('node1', 'node2')
G.add_edge('node1', 'node3')
G.add_edge('node1', 'node4')
G.add_edge('node1', 'node5')
G.add_edge('node1', 'node6')
G.add_edge('node1', 'node7')
G.add_edge('node2', 'node4')
G.add_edge('node4', 'node6')
G.add_edge('node6', 'node2')
G.add_edge('node7', 'node3')
G.add_edge('node3', 'node5')
G.add_edge('node5', 'node7')

#add position to display
pos = nx.spring_layout(G)

#draw serttings
fig = plt.figure(figsize=(10,10))
ax = plt.subplot()
ax.set_title('Graph', fontsize=12)
nx.draw(G, pos, node_size=1500, with_labels=True, node_color='red', font_size=10, font_color='white')

#draw the graph
plt.tight_layout()


#plot
path= r"C:\Users\tperez\Desktop\Session 2 PY\session02\images"
plt.savefig(path, format="PNG")