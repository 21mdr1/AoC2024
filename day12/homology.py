import numpy as np
from math import sqrt

NEG = False; POS = True

def distance(node1, node2):
    x1, y1 = node1; x2, y2 = node2
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

class Node():
    # 0-simplex
    def __init__(self, node1, pos = POS):
        self.node = node1
        self.pos = pos
    
    # node1 = node2
    def __eq__(self, other) -> bool:
        if not isinstance(other, Node):
            return False
        return self.node == other.node and self.pos == other.pos
    
    def __neg__(self):
        return Node(self.node, not self.pos)
    
    def __str__(self):
        if not self.pos:
            return f'- [ {self.node}]'
        return f'[ {self.node} ]'

class Edge():
    # 1-simplex
    def __init__(self, node1, node2, pos = POS):
        self.node1 = node1
        self.node2 = node2
        self.pos = pos

    def boundary(self) -> list[Node]:
        return [ Node(self.node1), Node(self.node2, NEG) ]
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Edge):
            return False
        return self.node1 == other.node1 and self.node2 == other.node2
    
    def __neg__(self):
        return Edge(self.node2, self.node1)

    def __str__(self):
        if not self.pos:
            return f'- [ {self.node1} {self.node2}]'
        return f'[ {self.node1} {self.node2} ]'

    
class Triangle():
    # 2-simplex
    def __init__(self, node1, node2, node3, pos = POS):
        self.node1 = node1
        self.node2 = node2
        self.node3 = node3
        self.pos = pos
    
    def boundary(self) -> list[Edge]:
        return [ Edge(self.node1, self.node2), Edge(self.node2, self.node3), Edge(self.node3, self.node1) ]

    def __eq__(self, other) -> bool:
        if not isinstance(other, Triangle):
            return False
        if self.node1 == other.node1 and self.node2 == other.node2 and self.node3 == other.node3:
            return True
        if self.node1 == other.node2 and self.node2 == other.node3 and self.node3 == other.node1:
            return True
        if self.node1 == other.node3 and self.node2 == other.node1 and self.node3 == other.node2:
            return True
        return False
    
    def __neg__(self):
        return Triangle(self.node1, self.node3, self.node2)

    def __str__(self):
        if not self.pos:
            return f'- [ {self.node1} {self.node2} {self.node3} ]'
        return f'[ {self.node1} {self.node2} {self.node3} ]'

def find_nodes(nodes):
    return [ Node(node) for node in nodes ]

def find_edges(nodes, dist):
    edges = []

    for node1, node2 in [ (a, b) for a in nodes for b in nodes ]:
        if node1 != node2 and distance(node1, node2) <= dist and Edge(node1, node2) not in edges and Edge(node2, node1) not in edges:
            edges.append(Edge(node1, node2))

    return edges

def find_triangles(nodes, dist):
    triangles = []

    for node1, node2, node3 in [ (a, b, c) for a in nodes for b in nodes for c in nodes ]:
        if node1 == node2 or node2 == node3 or node3 == node1:
            continue
        if distance(node1, node2) <= dist and distance(node2, node3) <= dist and distance(node3, node1) <= dist \
            and Triangle(node1, node2, node3) not in triangles and Triangle(node1, node3, node2) not in triangles:
            triangles.append(Triangle(node1, node2, node3))
    
    return triangles

class Matrix():
    def __init__(self, lst: list[list[int]]) -> int:
        self.value = np.array(lst)
    
    def create_blank(self, n, m):
        # check i'm getting the n and m right
        row = [0]*n
        return Matrix([ row for _ in range(m) ])
    
    def set(self, i, j, value):
        self.value[i][j] = value

    def rank(self) -> int:
        if self.value.size == 0:
            return 0

        return np.linalg.matrix_rank(self.value)

    def nullity(self) -> int:
        if self.value.size == 0:
            return 0
        return self.value.shape[1] - self.rank()
    
    def __repr__(self):
        return f'Matrix({self.value})'

def holes(nodes: list[Node], edges: list[Edge], triangles: list[Triangle] = None) -> int:
    if triangles is None or len(triangles) == 0: 
        array1 = []
    else:
        array1 = [ [0]*len(triangles) for _ in range(len(edges)) ]

        for i, triangle in enumerate(triangles):
            for boundaryEdge in triangle.boundary():
                for j, edge in enumerate(edges):
                    if boundaryEdge == edge:
                        array1[j][i] = 1
                    elif boundaryEdge == -edge:
                        array1[j][i] = -1

    array2 = [ [0]*len(edges) for _ in range(len(nodes)) ]

    for i, edge in enumerate(edges):
        for boundaryNode in edge.boundary():
            for j, node in enumerate(nodes):
                if boundaryNode == node:
                    array2[j][i] = 1
                if boundaryNode == -node:
                    array2[j][i] = -1

    matrix1 = Matrix(array1)
    matrix2 = Matrix(array2)

    return matrix2.nullity() - matrix1.rank()

def homology(points, dist):
    nodes = find_nodes(points)
    edges = find_edges(points, dist)
    triangles = find_triangles(points, dist)
    
    return holes(nodes, edges, triangles)