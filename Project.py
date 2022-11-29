from collections import namedtuple

State = namedtuple("State", ["a", "b", "c"])

# Constants
NOT_VISITED = 0
BEING_VISITED = 1
VISITED = 2


class Node:
    # The Node class for a Singly LinkedList is implemented. Do not change anything in this class.

    def __init__(self, val, next = None):
        self.val = val
        self.next = next


    def __repr__(self):
        return str(self)


class Queue:

    # Please implement each of the following methods in class Queue following the guide.
    # Here, I've only implemented the construction method and the dunder __repr__ method. Do not change them.

    def __init__(self):

        self.head = self.tail = None

    def empty(self):  # works
        # Return whether the Queue is empty or not.
        return self.head == None and self.tail == None

    def enqueue(self, item):  # works
        # Enqueue item to the tail of the Queue.
        # Note that, while enqueuing item to an empty Queue, both head and tail pointers need to be updated.
        # Do not return anything in the method.
        point = Node(item)
        if self.empty():
            self.head = point
            self.tail = point
        else:
            self.tail.next = point
            self.tail = point

    def dequeue(self):  # works
        assert not self.empty()
        # Dequeue the item at the head of the Queue.
        # Note that, after dequeuing the last item, both head and tail pointers need to be updated.
        # Return the dequeued item.
        value = self.head.val
        if self.head.next == None and self.tail.next == None:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        return value

    def __iter__(self):
        current = self.head
        while current != None:
            yield current
            current = current.next
    def __repr__(self):
        return "[" + ",".join(repr(n) for n in self) + "]"

class Stack:
    # Please implement each of the following methods in class Stack following the guide.
    # Here, I've only implemented the construction method and the dunder __repr__ method. Do not change them.

    def __init__(self):
        self.top = None

    def empty(self):
        # Return whether Stack is empty or not
        return self.top == None

    def push(self, item):
        # Push item to the top of the Stack.
        part = Node(item,self.top)
        self.top = part

    def pop(self):
        assert not self.empty()
        value = self.top.val
        self.top = self.top.next
        return value


    def __iter__(self):

        current = self.top
        while not current == None:
            yield current
            current = current.next

    def __repr__(self):
        # This implements "print Stack"

        ####################    DO NOT CHANGE THIS  ####################
        return "[" + ",".join(repr(n) for n in self) + "]"
class Vertex:
    def __init__(self, value: State):
        self.val: State = value
        self.neighbors = []
        self.distance = 0
        self.color = NOT_VISITED
        self.predecessor = None

    def set_color(self, new_color):
        self.color = new_color

    def get_color(self):
        return self.color

    def set_predecessor(self, pred):
        self.predecessor = pred

    def get_predecessor(self):
        return self.predecessor

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def add_neighbors(self, value):
        self.neighbors.append(value)

    def get_children(self):
        return self.neighbors

    def get_value(self):
        return self.val


class Graph:
    def __init__(self):
        self.vertex_dict = {}
        self.num_vertexes = 0
        self.cups: State = State(0, 0, 0)

    def add_vertex(self, val: tuple[int, int, int]):
        self.num_vertexes += 1
        new_vertex = Vertex(State(*val))
        self.vertex_dict[val] = new_vertex

    def __contains__(self, item):
        return item in self.vertex_dict

    def add_edge_from_v1_v2(self, v1, v2):
        if v1 not in self.vertex_dict:
            self.add_vertex(v1)
        if v2 not in self.vertex_dict:
            self.add_vertex(v2)
        self.vertex_dict[v1].add_neighbors(self.vertex_dict[v2])

    def get_vertexes(self):
        return self.vertex_dict.keys()

    def breath_first_search(self, target):
        # Initialization
        self.add_vertex((0, 0, 0))
        start = self.vertex_dict[(0, 0, 0)]
        start.set_distance(0)
        start.set_predecessor(None)
        start.set_color("black")
        q = Queue()

        q.enqueue(start)

        # While there are nodes to visit
        while not q.empty():
            vertex = q.dequeue()
            # Get path to target
            if target in vertex.get_value():
                path = []
                while vertex:
                    path.append((vertex.get_value()[0],vertex.get_value()[1],vertex.get_value()[2]))
                    vertex = vertex.predecessor
                path.reverse()
                return path

            # Go through edge nodes
            for child in new_state(vertex.val, self.cups):
                if child not in self.vertex_dict:
                    self.add_vertex(child)
                child = self.vertex_dict[child]
                if child.get_color() == NOT_VISITED:
                    child.set_color(BEING_VISITED)
                    #i.set_distance(v.get_distance() + 1)
                    child.set_predecessor(vertex)
                    q.enqueue(child)

            # Finalize visitation
            vertex.set_color(VISITED)
        return []

    def __iter__(self):
        return iter(self.vertex_dict.values())


def new_state(state: State, cups: State):

    a_to_b = min(state.a, cups.b - state.b)
    a_to_c = min(state.a, cups.c - state.c)
    b_to_a = min(state.b, cups.a - state.a)
    b_to_c = min(state.b, cups.c - state.c)
    c_to_b = min(state.c, cups.b - state.b)
    c_to_a = min(state.c, cups.a - state.a)
    x = [
        (cups.a, state.b, state.c),
        (state.a, cups.b, state.c),
        (state.a, state.b, cups.c),
        (0, state.b, state.c),
        (state.a, 0, state.c),
        (state.a, state.b, 0),
        (state.a - a_to_b, state.b + a_to_b, state.c),
        (state.a - a_to_c, state.b, state.c + a_to_c),
        (state.a + b_to_a, state.b - b_to_a, state.c),
        (state.a, state.b - b_to_c, state.c + b_to_c),
        (state.a, state.b + c_to_b, state.c - c_to_b),
        (state.a + c_to_a, state.b, state.c - c_to_a)
    ]
    x = set(x)
    x.add(state)
    x.remove(state)
    return x
def main():


    state1 = State(int(input("Bucket 1:")), int(input("Bucket 2:")), int(input("Bucket 3:")))

    target = int(input("Desired amount of water:"))

    g = Graph()
    g.cups = state1

    x = g.breath_first_search(target)

    print(x)
main()
