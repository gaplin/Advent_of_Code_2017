class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prev = self
        self.next = self

    def __str__(self) -> str:
        return '[{}, {}, {}]'.format(self.prev.value, self.value, self.next.value)
    
    def __repr__(self) -> str:
        return self.__str__()
    
def move(start: Node, steps: int) -> Node:
    for i in range(steps):
        start = start.next

    return start

def add_after(old_node: Node, new_node: Node) -> None:
    next = old_node.next
    old_node.next = new_node
    new_node.prev = old_node
    new_node.next = next
    next.prev = new_node

step = int(open('input2.txt').read().strip())

current = Node(0)
for i in range(1, 2018):
    current = move(current, step)
    new_node = Node(i)
    add_after(current, new_node)
    current = new_node

print(current.next.value)    