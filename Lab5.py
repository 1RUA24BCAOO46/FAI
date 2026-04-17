import heapq
h = []
heapq.heappush(h, 10)
heapq.heappush(h, 5)
heapq.heappush(h, 20)
h
[5, 10, 20]
step 1: Define graph

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2), ("E", 5)],
    "C": [("F", 3)],
    "D": [("G", 3)],
    "E": [("G", 1)],
    "F": [("G", 6)],
    "G": []
}
graph
{'A': [('B', 1), ('C', 4)],
 'B': [('D', 2), ('E', 5)],
 'C': [('F', 3)],
 'D': [('G', 3)],
 'E': [('G', 1)],
 'F': [('G', 6)],
 'G': []}
step 2: UCS functions

def ucs(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))
    visited = set()
    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        
        if node == goal:
            return path, cost
        
        if node in visited:
            continue
        
        visited.add(node)

        for neighbour, edge_cost in graph[node]:
            if neighbour not in visited:
                new_cost = cost + edge_cost
                new_path = path + [neighbour]
                heapq.heappush(priority_queue, (new_cost, neighbour, new_path))

    return None, None
step 3 : Run the search

start_node = "A"
goal_node = "G"

print("Running UCS from", start_node, "to", goal_node)

result_path, total_cost = ucs(graph, start_node, goal_node)

if result_path:
    print(f"Path Found : {result_path}")
    print(f"Total Cost : {total_cost}")
else:
    print("No path found!")
