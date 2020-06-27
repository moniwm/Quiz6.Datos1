from random import randint

from BST.BinarySearchTree import BinarySearchTree


def fillTree(bstTree, num=100):
    for i in range(num):
        element = randint(0, 1000)
        bstTree.insert(element)
    return bstTree


bstTree = BinarySearchTree()
bstTree = fillTree(bstTree)
bstTree.printTree()


