# -*- coding: utf-8 -*-

# 二叉树遍历
# 定义二叉树

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def create_BTree(root):
    input = raw_input('enter a tree data:\n')
    if input == '#':
        root = None
    else:
        root = TreeNode(input)
        if root.left is None:
            root.left = create_BTree(root.left)
        elif root.right is None:
            root.right = create_BTree(root.right)
    return root

def pre_order(root):
    if root is None:
        return
    print root.val
    pre_order(root.left)
    pre_order(root.right)

def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print root.val
    in_order(root.right)

def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print root.val


if __name__ == '__main__':
    root = None
    create_BTree(root)
    pre_order(root)
    in_order(root)
    post_order(root)
