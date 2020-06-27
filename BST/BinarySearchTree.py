from BST.Node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)
        else:
            print("The value is already in the tree")

    def findMin(self):
        if self.root is None:
            return None
        else:
            return self._findMin(self.root)

    def _findMin(self, node):
        if node is None:
            return None
        elif (node.left is None):
            return node
        else:
            return self._findMin(node.left)

    def remove(self, value):
        self.root = self._remove(value, self.root)

    def _remove(self, value, node):
        if node is None:
            return None
        if value < node.value:
            node.left = self._remove(value, node.left)
        elif value > node.value:
            node.right = self._remove(value, node.right)
        elif node.left is not None and node.right is not None:
            node.value = self._findMin(node.right)
            node.right = self._remove(node.value, node.right);
        else:
            if node.left is not None:
                node = node.left
            else:
                node = node.right
        return node


    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(str(node.value))
            self._printTree(node.right)




