class Tree(object):
    """Base class for a tree."""

    def __init__(self):
        """Create an empty Tree."""
        self.head = Node()


class Node:
    """Base class for a node in a tree, graph, etc."""

    def __init__(self, value=None):
        """Create a binary Node with two children."""
        self.value = value
        self.left = None
        self.right = None
