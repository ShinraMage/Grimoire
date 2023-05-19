# 遊戲編劇AI神助手02 HW-2


## PosetMage
use python convert markdown mindmap to image  
I need it automatically convert.  
you give me exmaple of input.md  
and give my python code to convert to out.png  

## GPT4

Unfortunately, I cannot convert your mindmap to an image directly here. However, I can guide you on how you might do this using Python. For this, you will need to use the networkx and matplotlib libraries to create the graph, and then save it as an image.  
The following is an example of creating a simple graph in Python using networkx:  
pythonCopy code  
```
import matplotlib.pyplot as plt
import networkx as nx

# Create a new graph
G = nx.Graph()

# Add nodes to the graph
G.add_node("Node 1")
G.add_node("Node 2")

# Add edge between the nodes
G.add_edge("Node 1", "Node 2")

# Draw the graph
nx.draw(G, with_labels=True)

# Save the graph as an image
plt.savefig("graph.png")
```
In this example, we create a graph G, add two nodes to it ("Node 1" and "Node 2"), add an edge between the nodes, and then draw the graph. The nx.draw function will automatically layout the nodes and edges in a nice way for most small to medium-sized graphs. Lastly, we use plt.savefig to save the image.  
This example is quite simple. In a real mind map, you would likely have many more nodes and edges, and you might want to customize the look of the nodes and edges. All of this is possible with networkx and matplotlib.  
Please note that this will be a simple rendering and may not suit all complex mind map requirements. For more complex visualizations, you might want to consider using dedicated graph visualization tools.  
  
## PosetMage
here is the problem:  
the output is one node at center and 7 subnodes all link to center.  
I think it is wrong.   

## GPT4
You're correct. My apologies for the oversight. The issue here is that the beautifulsoup library does not maintain the nested structure of the headers (h1, h2, h3, etc.) in the Markdown text.  
A more effective approach could be to parse the Markdown text directly without converting it to HTML. This way, we can preserve the nested structure of the headers by taking their levels into account (h1 being level 1, h2 being level 2, etc.).  
Here is an updated version of the script:  
pythonCopy code  

```
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Parse markdown
with open("input.md", "r") as f:
    lines = f.read().splitlines()

# Step 2: Create graph from parsed markdown
G = nx.DiGraph()
stack = []

for line in lines:
    level = line.count('#')
    label = line.replace('#', '').strip()
    node = (level, label)
    G.add_node(node)

    while stack and stack[-1][0] >= level:
        stack.pop()
    if stack:
        G.add_edge(stack[-1], node)
    stack.append(node)

# Step 3: Generate an image of the graph
plt.figure(figsize=(10,10))
pos = nx.spring_layout(G, seed=42)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos, node_size=500)

# edges
nx.draw_networkx_edges(G, pos, width=1)

# labels
labels = {node: node[1] for node in G.nodes}
nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, font_family='sans-serif')

plt.axis('off')
plt.savefig("out.png")  # save as png
plt.show()  # display

```

Now, your markdown will be interpreted in this way:  
•	Every header is a node. The level of the header (the number of # characters) represents the depth in the mindmap.  
•	A header is connected to the last header of one level above. For example, a level-2 header is connected to the last level-1 header that came before it.  
This should give you a more accurate representation of the mind map.  
  
