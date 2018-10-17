"""
Set 集合的特点是【无序且元素不重复，内部使用数组来存储元素】
一般具有以下几个操作,
    1. remove ，删除元素
    2. add， 增加元素
    3. has，判断元素是否存在
"""


class Set(object):
    def __init__(self, *args):
        self.data = []
        self.add(*args)

    def __repr__(self):
        return str(self.data)

    # 用来比较两个 Set实例 是否相等(==运算) 的魔法方法
    def __eq__(self, other):
        if len(self.data) != len(other.data):
            return False
        for d in other.data:
            if not self.has(d):
                return False
        return True

    def remove(self, x):
        if self.has(x):
            self.data.remove(x)
        return self.data

    def add(self, *args):
        for arg in args:
            # print(arg)
            if not self.has(arg):
                self.data.append(arg)
        return self.data

    def has(self, x):
        for d in self.data:
            if d == x:
                return True
        return False


def test_set():
    a = Set(1, 2, 2, 3, 4, 4)
    b = Set(1, 2, 2, 3, 4)
    c = Set(1, 3, 4, 2)
    d = Set(2, 3)
    assert (str(a) == '[1, 2, 3, 4]')
    print(a, b, c, d)
    assert (a == b)
    assert (a == c)
    assert (a != d)
    assert (a.has(1) == True)
    a.remove(1)
    assert (a.has(1) == False)
    a.add(1)
    assert (a.has(1) == True)


def test():
    test_set()


if __name__ == '__main__':
    test()

# todo: 参考 hash_table.py 的代码，写一个类 HashSet，实现时间复杂度为O(1) 的 add, remove 函数
# 形式如下：
# class HashSet(object):
#     # ...
#     def add(self, x):
#         pass
#
#     def remove(self, x):
#         pass
