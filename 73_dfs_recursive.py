# Graph traversal using DFS (Deapth first search)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}
count = 0
def dfs_traversal(graph,vertex,visited=None):
    global count 
    count = count + 1
    if visited==None:
        visited = set() #create set type variable 

    print(vertex,end=' ') #end=' ' output will be displayed on same line
    visited.add(vertex)

    # print(graph,vertex,visited)
    for neighbors in graph[vertex]:
        if neighbors not in visited:
            dfs_traversal(graph,neighbors,visited)
dfs_traversal(graph,'A')
size = len(graph)
print(f"No of time function executed = {count}")