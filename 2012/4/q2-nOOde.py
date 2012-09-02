class Node(object):
    def __init__(self, label):
        """Initialise a node with a given label"""
        self.label = label
        self.parent = None
        self.children = []

    def __str__(self):
        return self.pprint()

    def add_child(self, child):
        """
        Add a child node to the current node.
        * raises ValueError if child is None
        * raises TypeError if child is not a Node object
        * raises ValueError if child is already a child of the current node
        * raises ValueError if child already has its parent set
        """
        if isinstance(child, Node):
            if child.get_parent() != None:
                raise ValueError("Child already has parent")
            child.parent = self
            self.children.append(child)
        elif child == None:
            raise ValueError("Child cannot be None")
        else:
            raise TypeError("Child is not a Node object")

    def get_count(self):
        """Returns how many nodes are in the tree"""
        if len(self.children) == 0:
            return 1
        return 1 + sum(c.get_count() for c in self.children)

    def get_height(self):
        """Returns the height of the tree"""
        if len(self.children) == 0:
            return 1
        return 1 + max(c.get_height() for c in self.children)

    def get_label(self):
        """Returns the label of the current node"""
        return self.label

    def get_parent(self):
        """Returns the parent of the current node. Returns None if node does not have a parent"""
        return self.parent

    def has_ancestor(self, node):
        """Returns whether or not the current node has 'node' as an ancestor"""
        if self.parent == None:
            return False
        if self.parent == node:
            return True
        return self.parent.has_ancestor(node)

    def has_descendant(self, node):
        """Returns whether or not the current node has 'node' as a descendant"""
        if len(self.children) == 0:
            return False
        if node in self.children:
            return True
        return any(c.has_descendant(node) for c in self.children)

    def pprint(self):
        """Returns a string containing the nested 2-tuple representation of the tree"""
        if len(self.children) == 0:
            return '("{0}", ())'.format(self.label)
        return '("{0}", ({1}))'.format(self.label, ", ".join(str(c) for c in self.children))