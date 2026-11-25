def find_connected_components(number_of_vertices, edge_list):
    """
    Finds all connected components (separate groups) in an undirected graph.
    Vertices are numbered 0, 1, 2, ..., number_of_vertices - 1.
    """

    # ---------------------------------------------------------------
    # STEP 1: Build the neighbor's list for every vertex
    # ---------------------------------------------------------------
    # neighbours[x] will hold every vertex directly connected to x.
    # Start with an empty list for each vertex.
    neighbours = [[] for _ in range(number_of_vertices)] # 

    for vertex_a, vertex_b in edge_list:
        # print(vertex_a,vertex_b)
        # The graph is undirected, so a connection works both ways:
        neighbours[vertex_a].append(vertex_b)   # a can reach b
        neighbours[vertex_b].append(vertex_a)   # b can reach a

    # print(neighbours)
    # ---------------------------------------------------------------
    # STEP 2: Prepare the tracking variables
    # ---------------------------------------------------------------
    # is_visited[x] becomes True once vertex x has been reached.
    is_visited = [False] * number_of_vertices
    # print(is_visited)
    # exit(1)
    # all_components will hold every group we find.
    all_components = []

    # ---------------------------------------------------------------
    # STEP 3: Check every vertex, one by one
    # ---------------------------------------------------------------
    for start_vertex in range(number_of_vertices): # 0 to 11 
        # start_vertex will be 0 1 2 3 4 5 6 7 8 9 10 11
        # If this vertex was already reached by an earlier search,
        # it belongs to a group we already found, so skip it.
        if is_visited[start_vertex]:
            continue

        # Not visited yet, so this vertex starts a NEW group.
        current_component = []                  # 0 vertices in this new group
        vertices_to_explore = [start_vertex]    # 0 our "to-do" stack
        is_visited[start_vertex] = True

        # Keep exploring until there is nothing left to explore.
        while vertices_to_explore: #nested loop [1]

            # Take the most recently added vertex from the to-do stack.
            current_vertex = vertices_to_explore.pop() #0

            # It is part of this group.
            current_component.append(current_vertex)

            # Look at each neighbour of the current vertex.
            for neighbour in neighbours[current_vertex]: #nested loop

                # Only add neighbours we have not seen before.
                if is_visited[neighbour] == False:
                    is_visited[neighbour] = True          # mark now so it is never added twice
                    vertices_to_explore.append(neighbour)

        # The to-do stack is empty: nothing more can be reached,
        # so this group is complete. Save it (sorted for neat output).
        current_component.sort()
        all_components.append(current_component)

    return all_components


# ---------------------------------------------------------------
# Example (Adjacency List)
# ---------------------------------------------------------------
connections = [
    (0, 1), (0, 2), (1, 3), (2, 3),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (8, 9), (9, 10)]

groups = find_connected_components(12, connections)

print("Number of connected components:", len(groups))
count = 1
for group in groups:
    print(f"Component {count} : {group}")
    count = count + 1
# edges = [(0,1),(0,2),(1,3),(2,3),(4,5),(5,6),(6,7),(7,4),(8,9),(9,10)]
# print(find_connected_components(12, edges))
# # [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10], [11]]