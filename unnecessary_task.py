class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, idx):
    # Ваш код тут
    pass


def test():
    node3 = Node(input(), None)
    node2 = Node(input(), node3)
    node1 = Node(input(), node2)
    node0 = Node(input(), node1)
    new_head = solution(node0, 1)
    print(new_head.value,
          new_head.next_item.value,
          new_head.next_item.next_item.value)


if __name__ == '__main__':
    test()
