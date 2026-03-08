class Node:
    def __init__(self, new_data) -> None:
        self.data: int = new_data
        self.next: Node = None
        self.bottom: Node = None


# Time O(N Log N) | Space O(N)
def flatten(root: Node) -> Node:
    if not root:
        return None

    unique_nodes: dict[int, Node] = {}
    visited: set[Node] = set()
    stack: list[Node] = [root]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)

            if current.data not in unique_nodes:
                unique_nodes[current.data] = current

            if current.next:
                stack.append(current.next)
            if current.bottom:
                stack.append(current.bottom)

    sorted_keys: list[int] = sorted(unique_nodes.keys())

    if not sorted_keys:
        return None

    new_head: Node = unique_nodes[sorted_keys[0]]
    current_ptr: Node = new_head

    for i in range(1, len(sorted_keys)):
        next_node: Node = unique_nodes[sorted_keys[i]]

        current_ptr.next = next_node
        current_ptr.bottom = None
        current_ptr = next_node

    current_ptr.next = None
    current_ptr.bottom = None

    return new_head


def print_list(node: Node) -> None:
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")


# Create a hard-coded linked list:
# 5 -> 10 -> 19 -> 28
# |    |     |
# V    V     V
# 7    20    22
# |          |
# V          V
# 8          50
# |
# V
# 30

head = Node(5)
head.bottom = Node(7)
head.bottom.bottom = Node(8)
head.bottom.bottom.bottom = Node(30)

head.next = Node(10)
head.next.bottom = Node(20)

head.next.next = Node(19)
head.next.next.bottom = Node(22)
head.next.next.bottom.bottom = Node(50)

head.next.next.next = Node(28)

head = flatten(head)  # 5 -> 7 -> 8 -> 10 -> 19 -> 20 -> 22 -> 28 -> 30 -> 50 -> None

print_list(head)
