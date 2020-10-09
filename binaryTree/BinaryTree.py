from collections import deque

from binaryTree.Node import Node


def isBST(n):
    return isBSTCompare(n, -256, 256)


def isBSTCompare(n, min, max):
    if n is None:
        return True
    print(f'Current Node value {n.value}')
    if n.value < min or n.value > max:
        return False
    if not ((n.left is not None and n.right is None) or (n.left is None and n.right is not None)):
        return isBSTCompare(n.left, min, n.value) and isBSTCompare(n.right, n.value + 1, max)
    return False


def inOrderTraversalIterative(n):
    stack = deque()
    while not len(stack) == 0 or n is not None:
        if n is not None:
            stack.append(n)
            n = n.left
        else:
            n = stack.pop()
            print(n.value, end=" ")
            n = n.right


def inOrderTraversalReccursive(n):
    if n is None:
        pass
    if n.left is not None:
        inOrderTraversalReccursive(n.left)

    print(n.value, end=" ")

    if n.right is not None:
        inOrderTraversalReccursive(n.right)


def preOrderTraversalReccursive(n):
    if n is None:
        pass
    print(n.value, end=" ")
    if n.left is not None:
        preOrderTraversalReccursive(n.left)
    if n.right is not None:
        preOrderTraversalReccursive(n.right)


def height(n):
    if n is None:
        return 0

    return 1 + max(height(n.left), height(n.right))


def invertBT(n):
    if n is None:
        pass


def mirrorBT(n):
    if n is None:
        return

    if n.left is not None or n.right is not None:
        temp = n.left
        n.left = n.right
        n.right = temp
    mirrorBT(n.left)
    mirrorBT(n.right)


def printBT(n):
    if n is None:
        return
    print(n.value, end=" ")
    printBT(n.left)
    printBT(n.right)


def leafNodePath(n, s):
    if n is None:
        pass
    if n.left is None and n.right is None:
        print(s, n.value)
        return
    s = s + str(n.value) + " ->"
    leafNodePath(n.left, s)
    leafNodePath(n.right, s)
