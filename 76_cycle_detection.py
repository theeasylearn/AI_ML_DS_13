def has_cycle_directed(total_vertices, edges):

    # Create an empty adjacency list for each vertex.
    adjacency_list = [[] for vertex in range(total_vertices)]

    # Add directed edges to the adjacency list.
    for source_vertex, destination_vertex in edges:
        adjacency_list[source_vertex].append(destination_vertex)

    # Define three possible states of a vertex.
    WHITE = 0  # Not visited
    GRAY = 1   # Currently being processed
    BLACK = 2  # Completely processed

    # Initially, all vertices are unvisited.
    vertex_colors = [WHITE] * total_vertices

    # Store vertices in the current DFS recursion path.
    current_path = []

    def dfs(current_vertex):

        # Mark the current vertex as being processed.
        vertex_colors[current_vertex] = GRAY

        # Add the current vertex to the DFS path.
        current_path.append(current_vertex)

        # Visit every neighboring vertex.
        for neighbor_vertex in adjacency_list[current_vertex]:

            # Case 1: Neighbor is GRAY.
            # A cycle has been detected.
            if vertex_colors[neighbor_vertex] == GRAY:

                # Find the starting position of the cycle.
                cycle_start_index = current_path.index(neighbor_vertex)

                # Extract only the vertices belonging to the cycle.
                cycle = current_path[cycle_start_index:]

                # Add the starting vertex again to complete the cycle.
                cycle.append(neighbor_vertex)

                return cycle

            # Case 2: Neighbor has not been visited.
            if vertex_colors[neighbor_vertex] == WHITE:

                # Recursively search for a cycle.
                cycle = dfs(neighbor_vertex)

                # If a cycle is found, return it.
                if len(cycle) > 0:
                    return cycle

        # All neighbors have been completely processed.
        vertex_colors[current_vertex] = BLACK

        # Remove the current vertex from the DFS path.
        # This operation is known as backtracking.
        current_path.pop()

        # No cycle was found.
        return []

    # Visit every vertex, including disconnected vertices.
    for start_vertex in range(total_vertices):

        if vertex_colors[start_vertex] == WHITE:

            cycle = dfs(start_vertex)

            if len(cycle) > 0:
                return cycle

    # No cycle exists anywhere in the graph.
    return []


# ------------------------------------------
# Example of a Directed Graph
# ------------------------------------------

total_vertices = 9

directed_edges = [
    (0, 2),
    (0, 1),
    (1, 3),
    (1, 4),
    (2, 3),
    (2, 7),
    (3, 8),
    (4, 5),
    (5, 6),
    (6, 4),
    (7, 8)
]

cycle = has_cycle_directed(total_vertices, directed_edges)

if len(cycle) > 0:
    print("Cycle found:", cycle)
else:
    print("No cycle found")