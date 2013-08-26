class Node:
  def __init__(self, id, label):
    """
    Initialise a node with a given id and label
    """
    self.id = id
    self.label = label
    self.adjList = []

  def __str__(self):
    """
    Return a string representation of the node
    as "(id: label), e.g. (4: Greg)"
    """
    return "(%s: %s)" % (self.id, self.label)

  def add_neighbour(self, neighbour, label):
    """
    Add a neighbour to this node with
    a given edge label
    e.g. x.add_neighbour(y, "brother")
    """
    self.adjList.append((neighbour, label))

  def get_neighbours(self, label):
    """
    Returns a list of node objects that are
    neighbours of this node with a given edge label
    Return an empty list if there are no neighbours
    with the given label
    Return all neighbours if label is None
    e.g. x.get_neighbours("brother")
    """
    if label == None:
        return [x[0] for x in self.adjList]
    return [x[0] for x in self.adjList if x[1] == label]

  def degree(self, label):
    """
    Returns the number of neighbours with a given
    edge label
    Return total number of neighbours
    if label is None
    """
    if label == None:
        return len(self.adjList)
    return len([x for x in self.adjList if x[1] == label])

  def has_neighbour(self, node, label):
    """
    Returns True if this node has 'node' as a
    neighbour with a given label, False otherwise
    Returns True if this node has 'node' as a
    neighbour if label is None, False otherwise
    """
    if label == None:
        return len([x for x in self.adjList if x[0] == node]) > 0
    return len([x for x in self.adjList if x[0] == node and x[1] == label]) > 0
