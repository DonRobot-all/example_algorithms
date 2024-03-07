class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, elem):
    # Ваш код тут
    pass


def test():
    node3 = Node("задача3", None)
    node2 = Node("задача2", node3)
    node1 = Node("задача1", node2)
    node0 = Node("задача0", node1)
    idx = solution(node0, input())
    print(idx)


if __name__ == '__main__':
    test()
