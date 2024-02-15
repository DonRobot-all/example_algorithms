class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node):
    # Ваш код тут


def test():
    node3 = Node(input(), None)
    node2 = Node(input(), node3)
    node1 = Node(input(), node2)
    node0 = Node(input(), node1)
    solution(node0)



if __name__ == '__main__':
    test()
