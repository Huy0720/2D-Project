class Graph:
    def __init__(self, vertices): 
        self.V = vertices
        self.G = dict()
        self.temp_scc = []
        self.final_list_of_scc = []

    def add_edge(self, bf, af):
        if bf in self.G:
            self.G[bf].append(af)
        else:
            self.G[bf] = [af]
    
    def dfs(self, vertex, visited):
        visited[vertex] = True
        self.temp_scc.append(vertex)

        if self.G.get(vertex, None):
            for neighbour in self.G[vertex]:
                if not visited[neighbour]:
                    self.dfs(neighbour, visited)

    
    # Function to perform dfs on the graph and add to the main stack
    def dfs_stack(self, vertex, visited, main_stack):
        visited[vertex] = True

        for neighbour in self.G.get(vertex, []):
            if not visited[neighbour]:
                self.dfs_stack(neighbour, visited, main_stack)

        # Add the current vertex to the main stack
        main_stack.append(vertex)

    
    # Function to get the transpose of the graph
    def transpose(self):
        # Add all of the vertices to the transposed graph
        transposed_graph = Graph(self.V)

        # Add the reverse of each directed edge to the reverse graph
        for vertex in self.G:
            for neighbour in self.G[vertex]:
                transposed_graph.add_edge(neighbour, vertex)

        return transposed_graph

    # Function to return all of the strongly-connected components of the graph
    def return_all_scc(self):
        main_stack = []
        visited = [False] * self.V  # Initialize all of the values with False, since we have not visited any nodes

        # Add vertices to the main stack in reverse topological order (according to their finishing times)
        for vertex in range(0, self.V):
            if not visited[vertex]:
                self.dfs_stack(vertex, visited, main_stack)

        g_transposed = self.transpose()  # Create the transpose of the graph

        visited = [False] * self.V  # Mark all the vertices as not visited again to prepare for our second round of DFS

        # Process all the vertices in the order defined by the main stack
        while main_stack:
            vertex = main_stack.pop()

            if not visited[vertex]:
                g_transposed.dfs(vertex, visited)
                self.final_list_of_scc.append(g_transposed.temp_scc)
                g_transposed.temp_scc = []

        return self.final_list_of_scc


class Korasaju:
    def __init__(self, vertices, clauses):
        self.graph = Graph(int(vertices) * 2)
        self.vertices_list = []
        self.clauses_list = []
        self.largest_scc = []
        self.transformed_list = []
        self.map = dict()
        self.value = 0

        # Build list of vertices
        for vertex in range(1, int(vertices) + 1):
            self.vertices_list.append(vertex)
            self.vertices_list.append(-vertex)

        # Build map
        for vertex in self.vertices_list:
            self.map[vertex] = self.value
            self.value += 1

        self.reverse_map = {v:k for k,v in self.map.items()}  # Build reverse map

        # Build implication graph by drawing directed edges using the clauses
        for clause in clauses:
            # Ensure that it is a 2SAT problem
            if len(clause) != 2:
                continue

            # For a sample clasue A V B
            self.graph.add_edge(self.map[-int(clause[0])], self.map[int(clause[1])])  # Add edge ¬A -> B 
            self.graph.add_edge(self.map[-int(clause[1])], self.map[int(clause[0])])  # Add edge ¬B -> A 

        self.list_of_scc = self.graph.return_all_scc()  # Find all strongly-connected components

        for list_scc in self.list_of_scc:
            temp = [self.reverse_map[i] for i in list_scc]
            self.transformed_list.append(temp)

    def satisfiable(self):
        # Iterate thru every SCC and check if both xi and -xi exists in the same SCC. if it does, formula is unsatisfiable
        for scc in self.transformed_list:
            for literal in scc:
                if -literal in scc:
                    return False

        self.largest_scc = sorted(sorted(self.transformed_list, key = lambda j: len(j))[0], key = lambda k: max(k, -k))
        return True

    def sat_solve(self):
        if self.satisfiable():
            output = ""
            for element in self.largest_scc:
                if element < 0:
                    output += "1"
                elif element > 0:
                    output += "0"
                
                output += " "
            
            return "SATISFIABLE" + "\n" + output
        
        else:
            return "UNSATISFIABLE"
