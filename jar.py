class Jar:
    def __init__(self, capacity, quantity):
        self.capacity = capacity
        self.quantity = quantity
        if self.quantity > self.capacity:
            self.quantity = self.capacity
    def __repr__(self):
        return str(self.quantity)
    def __eq__(self, other: "Jar"):
        return self.capacity == other.capacity and self.quantity == other.quantity
    def copy(self):
        return Jar(self.capacity, self.quantity)
    def isFull(self):
        return self.quantity == self.capacity
    def isEmpty(self):
        return self.quantity == 0
    def fill(self):
        self.quantity = self.capacity
    def empty(self):
        self.quantity = 0
    def pour(self, other: "Jar"): #assumes that other jar is not full
        availableSpace = other.capacity - other.quantity
        if self.quantity < availableSpace:
            other.quantity += self.quantity
            self.quantity = 0
        else: #if self.quantity >= availableSpace
            other.quantity += availableSpace
            self.quantity -= availableSpace


class State:
    def __init__(self, jars: []):
        self.jars = jars
        self.neighbors = []
    def __repr__(self):
        return str(self.jars)
    def __eq__(self, other: "State"):
        assert len(self.jars) == len(other.jars)
        b = True
        for i in range(len(self.jars)):
            if self.jars[i] != other.jars[i]:
                b = False
        return b
    def copy(self):
        return State([jar.copy() for jar in self.jars])
    def simulate(self):
        #fills
        for i in range(len(self.jars)):
            possibleState = self.copy()
            possibleState.jars[i].fill()
            if self != possibleState and possibleState not in self.neighbors:
                self.neighbors.append(possibleState)
        #empties
        for i in range(len(self.jars)):
            possibleState = self.copy()
            possibleState.jars[i].empty()
            if self != possibleState and possibleState not in self.neighbors:
                self.neighbors.append(possibleState)
        #pours
        """for i in range(len(self.jars)):  
            for 
            possibleState = self.copy()

            if self != possibleState and possibleState not in self.neighbors:
                self.neighbors.append(possibleState)"""


j1 = Jar(3,0)
j2 = Jar(5,0)
j3 = Jar(7,0)
s = State([j1, j2, j3])
s.simulate()
print(s, s.neighbors)
for neighbor in s.neighbors:
    neighbor.simulate()
    print(neighbor, neighbor.neighbors)