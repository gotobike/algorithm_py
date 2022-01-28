# 11.ex1
# 迭代方式
def traverse(arr: list):
    for i in range(len(arr)):
        print(arr[i])


# 11.ex2
# 单链表节点：
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# 迭代访问
def traverse(self):
    p = self.__head
    while p:
        print(p.val)
        p = p.next


# 递归访问
def traverse(self):
    traverse(self.__head.next)


# 二叉树遍历框架，非线性递归遍历
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(self, root: TreeNode):
    traverse(root.left)
    traverse(root.right)
