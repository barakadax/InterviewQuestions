class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


# Time O(N) | Space O(1) - Floyd’s Cycle-Finding Algorithm
def removeLoop(head: Node | None) -> None:
    if not head or not head.next:
        return

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return

    slow = head
    if slow == fast:
        while fast.next != slow:
            fast = fast.next
    else:
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next

    fast.next = None


head = Node(1)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(7)
head.next.next.next.next = head.next
removeLoop(head)
