class Vertex:
    def __init__(self, value):
        self.val = value
        self.neighbors = []


    def addNeighbors(self, value):
        self.neighbors.append(value)


    def __str__(self):
        return str(self.val) + " is connected with: " + str([i for i in self.neighbors])


    def getconnectedTo(self):
        return [i for i in self.neighbors]


    def getValue(self):
        return self.val

class Graph:
    def __init__(self):
        self.vertex_dict = {}
        self.num_vertex = 0

    def addVertex(self, val):
        self.num_vertex += 1
        new_vertex = Vertex(val)
        self.vertex_dict[val] = new_vertex

    def __contains__(self, item):
        return item in self.vertex_dict

    def getVertex(self, n):
        if n in self.vertex_dict:
            return self.vertex_dict[n]
        else:
            return None

    def addEdge(self,v1,v2):
        if v1 not in self.vertex_dict:
            self.addVertex(v1)
        if v2 not in self.vertex_dict:
            self.addVertex(v2)
        self.vertex_dict[v1].addNeighbor(self.vertex_dict[v2])
        self.vertex_dict[v2].addNeighbor(self.vertex_dict[v1])
    def getVertexes(self):
        return self.vertex_dict.keys()

    def __iter__(self):
        return iter(self.vertex_dict.values())


