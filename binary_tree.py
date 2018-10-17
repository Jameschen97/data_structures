class Tree(object):
    def __init__(self, element=None):
        self.element = element
        self.left = None
        self.right = None

    def traversal(self):
        """
        树的遍历, 是一个递归操作
        """
        print(self.element)
        if self.left is not None:
            self.left.traversal()
        if self.right is not None:
            self.right.traversal()

    def reverse(self):
        """
        树的翻转
        """
        self.left, self.right = self.right, self.left
        if self.left is not None:
            self.left.reverse()
        if self.right is not None:
            self.right.reverse()


def test():
    # 手动构建二叉树
    t = Tree(0)
    left = Tree(1)
    right = Tree(2)
    t.left = left
    t.right = right
    left.left = Tree(3)
    left.right = Tree(4)
    right.left = Tree(5)
    right.right = Tree(6)
    # 遍历
    t.traversal()
    print('--------\n')
    t.reverse()
    t.traversal()


if __name__ == '__main__':
    test()
