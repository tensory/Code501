from .tree import Tree, Node

All you need to know to delete is:
    locate the right successor
    maintain a reference to the successor's parent P
    p.left = s.right
    q:q

class BinarySearchTree(Tree):
    def __init__(self):
        """Create an empty BinarySearchTree."""
        super(BinarySearchTree, self).__init__()

    def put(self, value, parent=None):
        """Insert a value into the tree.
        Insert the value as the head of the tree
        if the tree is empty;
        otherwise, insert it in the correct subtree.
        """
        if not parent:
            parent = self.head

        if parent.left is not None and value < parent.left.value:
            return put(self, value, parent.left)
        elif parent.right is not None and value > parent.right.value:
            return put(self, value, parent.right)
        else:
            parent.value = value
            return parent

    def delete(self, value):
        """Find a value, and if found, delete its
        containing Node.
        If the Node containing the value
        was a root node of a subtree,
        insert its children in the main tree
        using Hibbard's right successor algorithm.
        """
        t = find(self, value)
        x = find_right_successor(t.right)
        x.right = delete_min(t.right)
        x.left = t.left


    def find(self, value, parent=None):
        """Find a Node containing a value,
        if it exists in the tree.

        Returns
        -------
        node: the found Node
        """
        if parent is None:
            parent = self.head
        if parent.left is not None and value < parent.left.value:
            return find(self, value, parent.left)
        if parent.right is not None and value > parent.right.value:
            return find(self, value, parent.right)
        if parent.value == value:
            return parent
        return None


    def find_right_successor(self, node):
        """Find the leftmost node in a subtree.
        Pass a right child of a node to this method.
        """
        if node.left is None:
            return node
        return find_right_successor(self, node.left)


    def delete_min(self, node):
        """Recursively find a node that has a null left link
        and return its right child."""
        #
        #if node.left is None:
        #    return node.right
        #node.left = delete_min(self, node.left)
        #return node
        return find_right_successor(node).right


    def get_value(self, node):
        """Return a node's value."""
        return node.value
