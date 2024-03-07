class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def solution(node):
    # Ваш код тут
    pass


def test():
    node0 = DoubleConnectedNode(input())
    node1 = DoubleConnectedNode(input())
    node2 = DoubleConnectedNode(input())
    node3 = DoubleConnectedNode(input())
    node0.next = node1
    node1.prev = node0
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    new_head = solution(node0)
    print(new_head.value,
          new_head.next.value,
          new_head.next.next.value,
          new_head.next.next.next.value)


if __name__ == '__main__':
    test()
