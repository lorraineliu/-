# -*- coding: utf-8 -*-

# 二叉树遍历
# 定义二叉树

class TreeNode(object):
    def __init__(self, x=None, lnode=None,rnode=None):
        self.val = x
        self.left = lnode
        self.right = rnode

# 创建二叉树递归
def create_BTree(root, vals, i):
    if i < len(vals):
        if vals[i] == "#":
            return None
        else:
            root = TreeNode(x=vals[i])
            root.left = create_BTree(root.left, vals, 2*i+1)
            root.right = create_BTree(root.right, vals, 2*i+2)
            return root
    return root

# 前序
def pre_order(root):
    if root is None:
        return
    print root.val
    pre_order(root.left)
    pre_order(root.right)

# 中序
def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print root.val
    in_order(root.right)

# 后序
def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print root.val

# height
def height(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

# depth
def depth(root, tree_height):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return tree_height - height(root)
    return max(depth(root.left, tree_height), depth(root.right, tree_height)) - 1

# level
def level(root, tree_height):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return tree_height - height(root) + 1
    return max(level(root.left, tree_height), level(root.right, tree_height)) - 1

# BFS
def bfs_order(root):
    queue = []
    if root is None:
        return
    queue.append(root)
    while len(queue) > 0:
        visit = queue.pop(0)
        print visit.val
        if visit.left is not None:
            queue.append(visit.left)
        if visit.right is not None:
            queue.append(visit.right)


if __name__ == '__main__':
    root = None
    vals = ['1','2','3','#','4','5']
    root1 = create_BTree(root,vals, 0)
    height1 = height(root1)
    print "height: %d" % height1
    depth1 = depth(root1, height1)
    print "depth: %d" % depth1
    level1 = level(root1, height1)
    print "level: %d" % level1
    pre_order(root1)
    in_order(root1)
    post_order(root1)
    bfs_order(root1)
