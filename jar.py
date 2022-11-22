import copy

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
    def __init__(self, jar1, jar2, jar3):
        self.jar1 = jar1
        self.jar2 = jar2
        self.jar3 = jar3
        self.neighbors = []
    def __repr__(self):
        return str([self.jar1, self.jar2, self.jar3])
    def simulate(self):
        #fills
        jar1n = copy.deepcopy(self.jar1)
        jar1n.fill()
        if self.jar1 != jar1n:
            self.neighbors.append(State(copy.deepcopy(jar1n), copy.deepcopy(self.jar2), copy.deepcopy(self.jar3)))
        jar2n = copy.deepcopy(self.jar2)
        jar2n.fill()
        if self.jar2 != jar2n:
            self.neighbors.append(State(copy.deepcopy(self.jar1), copy.deepcopy(jar2n), copy.deepcopy(self.jar3)))
        jar3n = copy.deepcopy(self.jar3)
        jar3n.fill()
        if self.jar3 != jar3n:
            self.neighbors.append(State(copy.deepcopy(self.jar1), copy.deepcopy(self.jar2), copy.deepcopy(jar3n)))
        #empties
        
        #pours



j1 = Jar(3,0)
j2 = Jar(5,6)
j3 = Jar(7,0)
s = State(j1, j2, j3)
print(s.simulate())