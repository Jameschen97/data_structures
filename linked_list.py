class Node(object):
    def __init__(self, element=None, next=None):
        self.element = element
        self.next = next

    def __repr__(self):
        return str(self.element)


"""
不完整的链表实现
"""


class LinkedList(object):
    def __init__(self):
        self.head = None

    # O(1)
    def is_empty(self):
        return self.head is None

    def length(self):
        index = 0
        node = self.head
        while node is not None:
            index += 1
            node = node.next
        return index

    def find(self, element):
        node = self.head
        while node is not None:
            if node.element == element:
                break
            node = node.next
        return node

    def _node_at_index(self, index):
        i = 0
        node = self.head
        while node is not None:
            if i == index:
                return node
            node = node.next
            i += 1
        return None

    def element_at_index(self, index):
        node = self._node_at_index(index)
        return node.element

    # O(n)
    def insert_before_index(self, index, element):
        # 初始化一个 node
        node = Node(element)
        # 找到插入 node 的 前一个节点 n1
        n1 = self._node_at_index(index - 1)
        # 判断位于 index-1 的 node 是否存在
        if n1 is None:
            return False
        # 得到插入 node 的 后一个节点 n2
        n2 = n1.next
        # 插入 node
        n1.next = node
        node.next = n2

    # O(n)
    def insert_after_index(self, index, element):
        node = Node(element)
        n1 = self._node_at_index(index)
        if n1 is None:
            return False
        n2 = n1.next
        n1.next = node
        node.next = n2

    # 其实还可以这样写 insert_after_index()
    # def insert_after_index(self, index, element):
    #     self.insert_before_index(self, index + 1, element)

    # O(1)
    def first_object(self):
        first = self.head
        if first is not None:
            first = first.next
        return first

    # O(n)
    def last_object(self):
        last = self.head
        if last is not None:
            while last.next is not None:
                last = last.next
        return last

    # O(n)
    def append(self, node):
        if self.head is None:
            self.head = Node()
            self.head.next = node
        else:
            last_node = self.last_object()
            last_node.next = node
            # node.front = last_node


def log_list(linked_list):
    n = linked_list.head
    s = ''
    while n is not None:
        s += (str(n.element) + ' > ')
        n = n.next
    print(s)


def test():
    k = LinkedList()
    # k.first_object()
    # k.last_object()
    node = Node(1)
    k.append(node)
    node = Node(2)
    k.append(node)
    node = Node(3)
    k.append(node)
    log_list(k)


if __name__ == '__main__':
    test()
