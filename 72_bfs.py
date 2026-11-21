# Graph using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}
def bfs_traversal(graph,vertax):
    visited_node = set()
    queue = []
    if vertax in graph:
        print(vertax)
        visited_node.add(vertax)
        list = graph.get(vertax)
        queue.append(vertax)
        while len(queue)>0:
            temp = queue[0]
            list = graph.get(temp)
            for item in list: #b
                if item not in visited_node:
                    print(item) #b
                    visited_node.add(item) # a b
                    queue.append(item) # a b
            del queue[0]
bfs_traversal(graph,'A')