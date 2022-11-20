from Project import Vertex
"""john = Vertex(90)
john.addNeighbors(9)"""
mom = [1,2,3]
dad = [4,5,6]
john = Vertex(mom)
john.addNeighbors(dad)
print(john.getconnectedTo())
print(john.getconnectedTo()[0]==[4,5,6])
class j:
    def __init__(self, b):
        self.a = b
    def __eq__(self, other):
        return self.a == other.a
lebron = j(1)
james = j(1)
print(lebron == james)