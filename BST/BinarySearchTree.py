from BST.Node import Node

# Created by Monica Waterhouse Montoya

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.inOrderList = []
        self.preOrderList = []
        self.postOrderList = []

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
            return None
    def findMin(self):
        return self._findMin(self.root)

    def _findMin(self, node):
        if node is None:
            return None
        elif (node.left is None):
            return node
        else:
            return self._findMin(node.left)

    def findMax(self):
        return self._findMax(self.root)

    def _findMax(self, node):
        if node is None:
            return None
        elif (node.right is None):
            return node
        else:
            return self._findMax(node.right)

    def remove(self, value):
        self.root = self._remove(value, self.root)

    def _remove(self, value, node):
        if node is None:
            return None
        if value > node.value:
            node.right = self._remove(value, node.right)
        elif value < node.value:
            node.left = self._remove(value, node.left)
        elif node.left is not None and node.right is not None:
            node.value = self._findMin(node.right).value
            node.right = self._remove(node.value, node.right);
        else:
            if node.left is not None:
                node = node.left
            else:
                node = node.right
        return node

    def inOrder(self):
        if self.root is None:
            return None
        else:
            self._inOrder(self.root)

    def _inOrder(self,root):
        if root:
            self._inOrder(root.left)
            self.inOrderList.append(root.value)
            print(root.value)
            self._inOrder(root.right)

    def postOrder(self):
        if self.root is None:
            return None
        else:
            self._postOrder(self.root)

    def _postOrder(self, root):
        if root:
            self._postOrder(root.left)
            self._postOrder(root.right)
            print(root.value)
            self.postOrderList.append(root.value)

    def preOrder(self):
        if self.root is None:
            return None
        else:
            self._preOrder(self.root)

    def _preOrder(self, root):
        if root:
            print(root.value)
            self.preOrderList.append(root.value)
            self._preOrder(root.left)
            self._preOrder(root.right)

    def contains(self, value):
        return self._contains(value, self.root)

    def _contains(self, value, node):
        if node is None:
            return False
        else:
            if value < node.value:
                return self._contains(value, node.left)
            elif value > node.value:
                return self._contains(value, node.right)
            else:
                return True

    def getInOrderList(self):
        return self.inOrderList

    def getPreOrderList(self):
        return self.preOrderList

    def getPostOrderList(self):
        return self.postOrderList