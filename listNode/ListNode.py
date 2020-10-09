class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(node):
        while node:
            print(node.val, end=" ")
            node=node.next
        print("")

    def printListReversed(node):
        if node is None:
            return
        ListNode.printListReversed(node.next)
        print(node.val, end=" ")

    def reversingList(node):
        if not node:
            return
        prev=None
        while node:
            nextNode = node.next
            node.next=prev
            prev=node
            node=nextNode
        return prev

