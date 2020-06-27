from BST.Node import Node

# Created by Monica Waterhouse Montoya

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.in_order_list = []
        self.pre_order_list = []
        self.post_order_list = []

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
    def find_min(self):
        return self._find_min(self.root)

    def _find_min(self, node):
        if node is None:
            return None
        elif (node.left is None):
            return node
        else:
            return self._find_min(node.left)

    def find_max(self):
        return self._find_max(self.root)

    def _find_max(self, node):
        if node is None:
            return None
        elif (node.right is None):
            return node
        else:
            return self._find_max(node.right)

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
            node.value = self._find_min(node.right).value
            node.right = self._remove(node.value, node.right);
        else:
            if node.left is not None:
                node = node.left
            else:
                node = node.right
        return node

    def in_order(self):
        if self.root is None:
            return None
        else:
            self._in_order(self.root)

    def _in_order(self,root):
        if root:
            self._in_order(root.left)
            self.in_order_list.append(root.value)
            print(root.value)
            self._in_order(root.right)

    def post_order(self):
        if self.root is None:
            return None
        else:
            self._post_order(self.root)

    def _post_order(self, root):
        if root:
            self._post_order(root.left)
            self._post_order(root.right)
            print(root.value)
            self.post_order_list.append(root.value)

    def pre_order(self):
        if self.root is None:
            return None
        else:
            self._pre_order(self.root)

    def _pre_order(self, root):
        if root:
            print(root.value)
            self.pre_order_list.append(root.value)
            self._pre_order(root.left)
            self._pre_order(root.right)

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

    def get_in_order_list(self):
        return self.in_order_list

    def get_pre_order_list(self):
        return self.pre_order_list

    def get_post_order_list(self):
        return self.post_order_list