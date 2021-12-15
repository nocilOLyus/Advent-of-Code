from copy import deepcopy

with open("input.txt", "r") as f:
    data = [line.split('-') for line in f.read().split('\n')]

start_nodes = []
end_nodes = []
for index, line in enumerate(data):
    if 'start' in line:
        line.remove('start')
        start_nodes.append(line[0])
    elif 'end' in line:
        line.remove('end')
        end_nodes.append(line[0])
data = [line for line in data if len(line) != 1]

def make_nodes(data, start_nodes, end_nodes):
    d = deepcopy(data)
    nodes = {}
    for connection in d:
        for index, node in enumerate(connection):
            if node not in nodes:
                nodes[node] = []
                if node in end_nodes: nodes[node].append("END")
            nodes[node].append(connection[0 ** index])
            
    return nodes

nodes = make_nodes(data, start_nodes, end_nodes)
#print("nodes:", nodes)

visited_main = {}
def count_paths_per_node(to_visit, visited_min = [], part2 = False):
    global nodes, visited_main

    for node in to_visit:
        new_visit = visited_min + [node]
        paths = 0
        for next_node in nodes[node]:
            #print(f"looking at {next_node} from {node}")
            if next_node == "END":
                paths += 1

            elif not part2 and (next_node not in visited_min or next_node.isupper()):
                paths += count_paths_per_node([next_node], new_visit)

            elif part2:
                visited_twice = any([True for n in nodes if new_visit.count(n) > 1 and n.islower()])

                if next_node.isupper():
                    paths += count_paths_per_node([next_node], new_visit, part2 = True)

                elif (visited_twice and new_visit.count(next_node) < 1)\
                or (not visited_twice and new_visit.count(next_node) < 2):
                    paths += count_paths_per_node([next_node], new_visit, part2 = True)

        visited_main[new_visit[0]] = paths

    return paths

def total_paths(paths_per_node):
    return sum(paths_per_node.values())

# Part 1
count_paths_per_node(start_nodes)
#print("visited:", visited_main)
print("Part 1:", total_paths(visited_main), "paths.")

###
visited_main.clear()
###

# Part 2
count_paths_per_node(start_nodes, part2 = True)
print("Part 2:", total_paths(visited_main), "paths.")