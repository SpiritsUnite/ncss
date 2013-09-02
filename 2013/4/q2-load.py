from node import Node

class Graph:
  def __init__(self, label, filename):
    """
    Initialise a graph with a given label.
    If filename is not None, load the graph from the file
    """
    self.label = label
    self.ids = []
    self.nodes = {}
    self.neigh = {}
    if filename:
        self.load(filename)

  def size(self):
    """
    Return the number of nodes in the graph
    """
    return len(self.nodes)

  def load(self, filename):
    """
    Load the graph from the given filename.
    Raise ValueError if a node with a duplicate
    id is added or if a relationship between
    nonexisting nodes is created
    """
    self.ids = []
    self.nodes = {}
    self.neigh = {}
    f = open(filename)
    for line in f:
        if not line.strip(): break
        i, l = map(str.strip, line.split(':'))
        if i in self.nodes:
            raise ValueError
        self.nodes[i] = Node(i, l)
        self.neigh[i] = []
        self.ids.append(i)

    for line in f:
        fr, l, to = map(str.strip, line.split(':'))
        if not l: l = None
        if fr not in self.nodes or to not in self.nodes:
            raise ValueError
        self.nodes[fr].add_neighbour(self.nodes[to], l)
        if l == None: l = ''
        self.neigh[fr].append((to, l))

  def output(self):
    """
    Prints the graph with nodes listed in sorted order
    of ids with their neighbours and neighbour labels
    If neighbour labels are None, print the empty
    string.
    Print empty brackets if a node has no neighbours
    e.g.
    (0: Bob) [1:son, 2:wife]
    (1: John) [0:father, 2:mother]
    (2: Jane) [0:husband, 1:son]
    (3: Greg) [1:friend]
    """
    for i in sorted(self.nodes.keys()):
        print(self.nodes[i], '[%s]' % ', '.join(':'.join(x) for x in sorted(self.neigh[i])))

  def degrees_of_separation(self, n1, n2):
    """
    Returns the minimum degrees of separation from
    n1 to n2, where n1 and n2 are ids.
    Each x on the path between n1
    and n2 fulfills the has_neighbour relationship.
    Return -1 if n1 and n2 are not connected.
    Raise ValueError if either n1 or n2 is not in
    this graph
    If n2 is a neighbour of n1, then there is
    1 degree of separation.
    e.g. graph.degrees_of_separation(n1, n2)
    """
    if n1 not in self.nodes or n2 not in self.nodes:
        raise ValueError
    adjMat = [[1 if self.nodes[i].has_neighbour(self.nodes[j], None) else 1<<29
        for j in self.ids]
            for i in self.ids]
    for k in range(self.size()):
        for i in range(self.size()):
            for j in range(self.size()):
                adjMat[i][j] = min(adjMat[i][j], adjMat[i][k] + adjMat[k][j])

    a = adjMat[self.ids.index(n1)][self.ids.index(n2)]
    if a == 1<<29: a = -1
    return 0 if n1 == n2 else a

  def get_node(self, id):
    """
    Returns the node with the given id
    Raise ValueError if no node with the id exists
    """
    if id not in self.nodes:
        raise ValueError
    return self.nodes[id]
