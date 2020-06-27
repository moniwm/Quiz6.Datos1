import unittest

from BST.BinarySearchTree import BinarySearchTree
from BST.Node import Node

class Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.tree = BinarySearchTree()
        self.treeEmpty = BinarySearchTree()
        self.list = [17,14,86,77,25,63,9,22,1,15,24]
        for i in self.list:
            self.tree.insert(i)

    def testInsert(self):
        for i in self.list:
            self.assertTrue(self.tree.contains(i), True)
        self.assertEqual(self.tree.insert(77), None)

    def testFindMin(self):
        self.assertEqual(self.tree.findMin().value, 1)
        self.assertEqual(self.treeEmpty.findMin(), None)

    def testFindMax(self):
        self.assertEqual(self.treeEmpty.findMax(), None)
        self.assertEqual(self.tree.findMax().value, 86)


    def testRemove(self):
        self.tree.remove(14)
        self.assertEqual(self.tree.contains(14), False)
        self.tree.remove(25)
        self.assertEqual(self.tree.contains(25), False)
        self.tree.remove(9)
        self.assertEqual(self.tree.contains(9), False)
        self.assertEqual(self.treeEmpty.remove(2), None)


    def testInOrder(self):
        self.inOrderListExpected = [1,9, 14, 15,17,22,24,25,63,77,86]
        self.tree.inOrder()
        self.assertListEqual(self.tree.getInOrderList(), self.inOrderListExpected)
        self.assertEqual(self.treeEmpty.inOrder(), None)

    def testPreOrder(self):
        self.preOrderListExpected = [17, 14, 9, 1, 15, 86, 77, 25, 22, 24, 63]
        self.tree.preOrder()
        self.assertListEqual(self.tree.getPreOrderList(), self.preOrderListExpected)
        self.assertEqual(self.treeEmpty.preOrder(), None)

    def testPostOrder(self):
        self.postOrderListExpected = [1,9,15,14,24,22,63,25,77,86,17]
        self.tree.postOrder()
        self.assertListEqual(self.tree.getPostOrderList(), self.postOrderListExpected)
        self.assertEqual(self.treeEmpty.postOrder(), None)