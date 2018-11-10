"""
Create and visualize the network of foods and nutrients
"""
import networkx as nx
import matplotlib.pyplot as plt
import dzcnapy_plotlib as dzcnapy
import csv

with open("/home/chrisnelson/move/flowlogs-accept.log") as infile:
    csv_reader = csv.reader(infile)
    G = nx.Graph(csv_reader)
print(G.nodes())

loops = list(G.selfloop_edges())
G.remove_edges_from(loops)
print(loops)

mapping = {node: node.title() for node in G if isinstance(node, str)}
nx.relabel_nodes(G, mapping, copy=False)
print(G.nodes())

nutrients = set(("172.31.27.238","52.15.159.198","54.194.229.79","91.189.88.152","91.189.91.157","91.189.92.19","91.189.92.20","91.189.92.40","91.189.92.41"))

nutrient_dict = {node: (node in nutrients) for node in G}
nx.set_node_attributes(G, nutrient_dict, "nutrient")

# Prepare for drawing
colors = ["yellow" if n[1]["nutrient"] else "pink" for n in
          G.nodes(data=True)]
dzcnapy.medium_attrs["node_color"] = colors

# Draw four layouts in four subplots
_, plot = plt.subplots(2, 2)

subplots = plot.reshape(1, 4)[0]
layouts = (nx.random_layout, nx.circular_layout, nx.spring_layout,
           nx.spectral_layout)
titles = ("Random", "Circular", "Force-Directed", "Spectral")
for plot, layout, title in zip(subplots, layouts, titles):
    pos = layout(G)
    nx.draw_networkx(G, pos=pos, ax=plot, with_labels=False, 
                     **dzcnapy.medium_attrs)
    plot.set_title(title)
    dzcnapy.set_extent(pos, plot)

dzcnapy.plot("nutrients")

from networkx.drawing.nx_agraph import graphviz_layout

_, plot = plt.subplots()
pos = graphviz_layout(G)
nx.draw_networkx(G, pos, **dzcnapy.attrs)
dzcnapy.set_extent(pos, plot)
dzcnapy.plot("nutrients-graphviz")
