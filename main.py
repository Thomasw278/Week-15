
class Graph:
    def __init__(self):
        self.data = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.data:
            self.data[vertex] = []
            
    def vertex(self):
        for key in self.data.keys():
            print(key, end = " ")
        print()

    def add_edge(self, x, y):
        if x in self.data and y in self.data:
            self.data[x].append(y)
            self.data[y].append(x)
    
    def get_edges(self):
        list_edges = set()
        for vertex, neighbors in self.data.items():
            for neighbor in neighbors:
                if neighbor+vertex not in list_edges and vertex+neighbor not in list_edges:
                    list_edges.add(vertex+neighbor)
        return list(list_edges)
        # return sorted(list(list_edges))
    
    def dfs(self, node, y, visited, path):
        path.append(node)
        visited.append(node)
        if node == y:
            return path
        else:
            visits = 0
            for item in self.data[node]:
                if item not in visited:
                    visits += 1
                    self.dfs(item, y, visited, path)
            if visits == 0:
                path.pop()

    def find_path_dfs(self, x, y):
        visited = []
        path = []
        self.dfs(x, y, visited, path)
        if path[-1] != y:
            return
        return path
        

    def remove_edge (self, edge : str):
    #cara 1
        # edge = list(edge)
        # edge1 = edge[0]
        # edge2 = edge[1]
        # temp = self.data[edge1]
        # temp.remove(edge2)
        # self.data.pop(edge2)
        # self.data[edge1] = temp
    #cara 2
        # if len(edge) != 2:  # Edge harus terdiri dari dua karakter
        #     return
        # vertex1 = edge[0]
        # vertex2 = edge[1]
        # if vertex1 in self.data and vertex2 in self.data:  # Jika kedua vertex ada di graf
        #     if vertex2 in self.data[vertex1]:  # Jika vertex2 adalah tetangga vertex1
        #         self.data[vertex1].remove(vertex2)
        #     if vertex1 in self.data[vertex2]:  # Jika vertex1 adalah tetangga vertex2
        #         self.data[vertex2].remove(vertex1)   
    #Cara 3
        if len(edge) != 2:
            return
        vertex1,vertex2 = edge[0], edge[1]
        if vertex1 in self.data and vertex2 in self.data:
            #Hapus
            if vertex2 in self.data[vertex1]:
                self.data[vertex1].remove(vertex2)
            if vertex1 in self.data[vertex2]:
                self.data[vertex2].remove(vertex1)
            self.data[vertex1].sort()
            self.data[vertex2].sort()
    
    def remove_vertex(self, vertex):
    #cara 1
        self.data.pop(vertex)
        for keys,values in self.data.items():
            if vertex in values:
                values.remove(vertex)
    #cara 2
        # if vertex in self.data:  # Jika vertex ada di graf
        #     a = self.data[vertex]  # Tetangga dari vertex
        #     for b in a:  # Hapus vertex dari adjacency list setiap tetangga
        #         self.data[b].remove(vertex)
        #     del self.data[vertex]  # Hapus vertex dari graf
    #Cara 3
        # if vertex in self.data:
        #     a = self.data[vertex]
        #     for i in a:
        #         self.data[i].remove(vertex)
        #         self.data[i].sort()
        #     del self.data[vertex]

def main () :
    g : Graph = Graph()
    for i in ["a", "b", "c", "d", "e", "f", "g", "h"]:
        g.add_vertex(i)
    
    g.add_edge("a", "b")
    g.add_edge("a", "c")
    g.add_edge("a", "d")
    g.add_edge("a", "e")
    g.add_edge("a", "f")
    g.add_edge("d", "f")
    print("edges sebelum dihapus: ")
    print(g.get_edges()) 
    g.remove_edge("af")
    print()
    print("Edges setelah hapus edge af: ")
    print(g.get_edges())
    g.remove_vertex("a")
    print()
    print("Edges setelah hapus vertex a")
    print(g.get_edges())
if __name__ == "__main__":
    main()
