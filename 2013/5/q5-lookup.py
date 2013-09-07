from node import Node

class ParseException(Exception):
    pass

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

  def graph_search(self, node, query):
      tokens = query.split()
      nodes = n_query(tokens, node, self)
      if nodes == False:
          nodes = g_query(tokens, node, self)
      if nodes == False:
          raise ParseException
      if tokens:
          raise ParseException
      ans = list(nodes)
      ans.sort(key=lambda x: x.id)
      return ans

def pop(tokens, legal):
    if tokens and tokens[0].upper() in legal:
        tokens.pop(0)
        return True
    return False

def pope(tokens, legal):
    if not pop(tokens, legal): raise ParseException

def label_condition(tokens, node, nodes):
    if not pop(tokens, ["LABEL"]): return False
    if not tokens: raise ParseException
    l = tokens.pop(0)
    return set(n for n in nodes if n.label == l)

def node_label_condition(tokens, node, nodes):
    if not pop(tokens, ["NEIGHBOUR"]): return False
    if not pop(tokens, ["LABEL"]): raise ParseException
    if not tokens: raise ParseException
    l = tokens.pop(0)
    return set(n for n in nodes if node.has_neighbour(n, l))

def num_operator(tokens):
    if pop(tokens, ["EXACTLY"]):
        return "=="
    elif pop(tokens, ["LESS"]):
        if not pop(tokens, ["THAN"]): raise ParseException
        return "<"
    elif pop(tokens, ["MORE"]):
        if not pop(tokens, ["THAN"]): raise ParseException
        return ">"
    return False

def num(tokens):
    if not tokens: return False
    try:
        v = int(tokens[0])
    except ValueError:
        return ''
    tokens.pop(0)
    return v

def num_condition(tokens, node, nodes):
    op = num_operator(tokens)
    if not op: return False
    v = num(tokens)
    if v == '': raise ParseException
    if not pop(tokens, ["NEIGHBOURS"]): raise ParseException
    l = None
    if pop(tokens, ["WITH"]):
        if not pop(tokens, ["LABEL"]): raise ParseException
        if not tokens: raise ParseException
        l = tokens.pop(0)
    if op == '==':
        return set(n for n in nodes if n.degree(l) == v)
    elif op == '<':
        return set(n for n in nodes if n.degree(l) < v)
    return set(n for n in nodes if n.degree(l) > v)

def num_label_condition(tokens, node, nodes):
    op = num_operator(tokens)
    if not op: return False
    v = num(tokens)
    if v == '': raise ParseException
    if not pop(tokens, ["NEIGHBOURS"]): raise ParseException
    if not pop(tokens, ["WITH"]): raise ParseException
    if not pop(tokens, ["LABEL"]): raise ParseException
    if not tokens: raise ParseException
    l = tokens.pop(0)
    if op == '==':
        return set(n for n in nodes if n.degree(l) == v)
    elif op == '<':
        return set(n for n in nodes if n.degree(l) < v)
    return set(n for n in nodes if n.degree(l) > v)

def neighbour_num_condition(tokens, node, nodes):
    return num_condition(tokens, node, nodes)

def n_condition(tokens, node, nodes):
    a = label_condition(tokens, node, nodes)
    if a != False: return a
    a = node_label_condition(tokens, node, nodes)
    if a != False: return a
    a = neighbour_num_condition(tokens, node, nodes)
    if a != False: return a
    if not pop(tokens, ["("]): return False
    a = n_conditions(tokens, node, nodes)
    if not pop(tokens, [")"]): raise ParseException
    return a

def n_and_condition(tokens, node, nodes):
    a = n_condition(tokens, node, nodes)
    if a == False: return False
    if pop(tokens, ["AND"]):
        b = n_condition(tokens, node, nodes)
        if b == False: raise ParseException
        a.intersection_update(b)
    return a

def n_conditions(tokens, node, nodes):
    a = n_and_condition(tokens, node, nodes)
    if a == False: return False
    if pop(tokens, ["OR"]):
        b = n_and_condition(tokens, node, nodes)
        if b == False: raise ParseException
        a.update(b)
    return a

def n_query(tokens, node, graph):
    if pop(tokens, ["NEIGHBOURS"]):
        if not pop(tokens, ["WHO"]): raise ParseException
        if not pop(tokens, ["HAVE"]): raise ParseException
        return n_conditions(tokens, node, set(node.get_neighbours(None)))
    elif pop(tokens, ["ALL"]):
        if not pop(tokens, ["NEIGHBOURS"]): raise ParseException
        return node.get_neighbours(None)
    else:
        return False

def degree_condition(tokens, node, nodes, graph):
    v = num(tokens)
    if v == '': return False
    if not pop(tokens, ["DEGREES"]): raise ParseException
    if not pop(tokens, ["OF"]): raise ParseException
    if not pop(tokens, ["SEPARATION"]): raise ParseException
    if not pop(tokens, ["FROM"]): raise ParseException
    if not pop(tokens, ["ME"]): raise ParseException
    return set(n for n in nodes if graph.degrees_of_separation(node.id, n.id) == v)

def g_condition(tokens, node, nodes, graph):
    a = num_condition(tokens, node, nodes)
    if a != False: return a
    a = degree_condition(tokens, node, nodes, graph)
    if a != False: return a
    if not pop(tokens, ["("]): return False
    a = g_conditions(tokens, node, nodes, graph)
    if not pop(tokens, [")"]): raise ParseException
    return a

def g_and_condition(tokens, node, nodes, graph):
    a = g_condition(tokens, node, nodes, graph)
    if a == False: return False
    if pop(tokens, ["AND"]):
        b = g_condition(tokens, node, nodes, graph)
        if b == False: raise ParseException
        a.intersection_update(b)
    return a

def g_conditions(tokens, node, nodes, graph):
    a = g_and_condition(tokens, node, nodes, graph)
    if a == False: return False
    if pop(tokens, ["OR"]):
        b = g_and_condition(tokens, node, nodes, graph)
        if b == False: raise ParseException
        a.update(b)
    return a

def g_query(tokens, node, graph):
    if not pop(tokens, ["PEOPLE"]): return False
    if not pop(tokens, ["WHO"]): raise ParseException
    if not pop(tokens, ["HAVE"]): raise ParseException
    return g_conditions(tokens, node, graph.nodes.values(), graph)

