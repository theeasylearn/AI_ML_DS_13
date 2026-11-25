# Graph traversal using DFS (Depth first search) stack
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}
def graph_dfs_stack(graph,start):
    # print(graph,vertex)
    visited = set() #empty set 
    stack = [start] #create list which has initially only 'A
    
    #process stack until it is not empty 
    while stack:
        vertex = stack.pop() #fetch top most value in stack (a)
        if vertex not in visited:
            print(vertex,end=' ')
            visited.add(vertex)
        #fetch adjacency node of A
        for neighbor in reversed(graph[vertex]): # c b
            if neighbor not in visited:   
                stack.append(neighbor)         
graph_dfs_stack(graph,'A')
