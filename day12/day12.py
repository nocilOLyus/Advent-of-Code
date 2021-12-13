with open("example.txt", "r") as f:
    data = [line.split('-') for line in f.read().split('\n')]

start_nodes = []
# end_nodes = []
for index, line in enumerate(data):
    if 'start' in line:
        line.remove('start')
        start_nodes.append(line[0])
    # elif 'end' in line:
    #     line.remove('end')
    #     end_nodes.append(line[0])
data = [line for line in data if len(line) != 1]

def make_nodes(start_nodes):            # remake this, I want all the nodes faggot
    global data
    nodes = {}

    for node in start_nodes:
        if node not in nodes: nodes[node] = []
        for line in data:
            if node in line and len(line) != 1:
                line.remove(node)
                nodes[node].append(line[0])
    
    return nodes

def count_paths(starting_node):
    pass

print(start_nodes)
nodes = make_nodes(start_nodes)
for node, connections in nodes.items():
    count_paths((node, connections))