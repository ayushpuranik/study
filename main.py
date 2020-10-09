"""from greetings import Greetings

name = input("What is your name? ")
year = int(input("In which year you were born? "))

from agecalculator.AgeCalculator import AgeCalculator

ac = AgeCalculator()


print(f'{Greetings.sayHello(name)} You are {ac.getAge(year)} years old')
"""

# from factorial.Factorial import factorial as fact
# fact = fact()
# print(fact.factorial(6))

# from prime import Prime
# 
# for i in range(1,50):
#     print(i, Prime.isPrime(i))

# from pelindrome import Pelindrome
#
# print(Pelindrome.getPelindrome("Ayush"))


# num = 434566
#
#
# def getIntPelindrome(num):
#     digits = []
#     temp = num
#     while temp != 0:
#         digits.append(temp % 10)
#         temp = temp // 10
#     res = 0
#     for i in digits:
#         res = res * 10 + i
#     return res
#
#
# for i in range(1, 10000):
#     print(i, getIntPelindrome(i))


# from fibonacci.Fibonacci import fibonacci
#
# fibonacci(-10)


# from binaryTree.Node import Node
# from binaryTree import BinaryTree
# 
# """   5
#     /  \
#    2    7
#   / \  / \
#  1  3 6   8"""
# n0 = Node(0, None, None)
# n1 = Node(1, None, None)
# n2 = Node(3, None, None)
# n3 = Node(2, n1, n2)
# n4 = Node(6, None, None)
# n5 = Node(8, None, None)
# n6 = Node(7, n4, n5)
# n7 = Node(5, n3, n6)
# 
# # print(BinaryTree.height(n7))
# # n6=Node(6,None,None)
# # n7=Node(7,None,None)
# # n8=Node(5,n6,n7)
# 
# # print(BinaryTree.isBST(n7))
# 
# """
#        a
#      b   c
#    d  e f g
#      h m k
#      
#        a
#      c   b
#     g f e d
#      k m h   
# """
# 
# m = Node('m', None, None)
# k = Node('k', None, None)
# f = Node('f', m, k)
# g = Node('g', None, None)
# c = Node('c', f, g)
# h = Node('h', None, None)
# e = Node('e', h, None)
# d = Node('d', None, None)
# b = Node('b', d, e)
# a = Node('a', b, c)
# 
# 
# # BinaryTree.inOrderTraversalReccursive(a)
# # print("\n**")
# # BinaryTree.preOrderTraversalReccursive(a)
# # print("\n")
# # print(BinaryTree.height(a))
# #
# # BinaryTree.printBT(n7)
# # print("\n**")
# # BinaryTree.mirrorBT(n7)
# # print("**")
# # BinaryTree.printBT(n7)
# # print("\n------")
# 
# # BinaryTree.leafNodePath(n7,"")
# # BinaryTree.inOrderTraversalIterative(a)


# def maxCount(m, n, ops):
#     M = [[0] * m] * n
#     print(M)
#     for item in ops:
#         for i in range(0, item[0]):
#             M[i][0] += 1
#         for j in range(0, item[1]):
#             M[0][j] += 1
#     print(M)
#
#
# maxCount(3,3,[[2,2],[3,3]])
#

# from ishappy.isHappy import Solution
# Solution().isHappy(19)


def maxSubArray(nums):
    m = nums[0]
    for i in range(0, len(nums) - 1):
        s = nums[i]
        for j in range(i + 1, len(nums)):
            s = s + nums[j]
            m = max(m, s, nums[j])
    return m

    # print(maxSubArray([-2, 1]))
    # z,nz
    # 0,1,0,3,12

    # def moveZeroes(nums):
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     z, nz = 0, 0
    #     while nz < len(nums):
    #         if (nums[z] != 0):
    #             z += 1
    #             continue
    #         nz = z + 1;
    #         while (nums[nz] == 0):
    #             nz += 1
    #
    #         t = nums[z]
    #         nums[z] = nums[nz]
    #         nums[nz] = nums[z]
    #
    #     print(nums)
    #
    #
    # moveZeroes([0, 1, 0, 3, 12])


# from collections import deque
#
#
# def backspaceCompare(S, T):
#     s = deque()
#     t = deque()
#
#     for ch1 in S:
#         if ch1 == '#':
#             if len(s) > 0:
#                 s.pop()
#         else:
#             s.append(ch1)
#
#     for ch2 in T:
#         if ch2 == '#':
#             if len(t) > 0:
#                 t.pop()
#         else:
#             t.append(ch2)
#
#
#     return s == t
# "xywrrmp"
# "xywrrmu#p"
#
# print(backspaceCompare("xywrrmp", "xywrrmu#p"))

# def lastStoneWeight(stones):
#     while len(stones) >0:
#         m1=max(stones)
#         stones.remove(m1)
#         m2=max(stones)
#         stones.remove(m2)
#         if m1 - m2 > 0:
#             stones.append(m1 - m2)
#     print(stones)
#
# lastStoneWeight([2,2])


# def isSubPath(head, root) -> bool:
#     if head is None and root is None:
#         return True
#     stack = []
#     while not (root.value == head.value):
#         stack.append(root)
#
#         if root.left is not None:
#             root = root.left
#         else:
#             root = stack.pop()
#             root = root.right
#
#     if root is None:
#         return False
#
#     if root.value == head.value:
#         if isSubPath(head.next, head.left) or isSubPath(head.next, head.right):
#             return True
#         return False


from listNode.ListNode import ListNode

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
ListNode.printList(head)
print("## printing linked list values in reverse ##")
ListNode.printListReversed(head)
print("")
print("## Reversing a linked list ##")
ListNode.printList(ListNode.reversingList(head))
