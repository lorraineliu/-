# -*- coding: utf-8 -*-

cache_size = 10

class LinkedNode(object):
    def __init__(self, val):
        self.value = val
        self.next = None

def init_linked_nodes(size):
    head = next = LinkedNode(0)
    for i in xrange(1, size):
        node = LinkedNode(i)
        next.next = node
        next = node
    return head

def len_of_linked_nodes(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def lru_by_linked_node(head, value):
    if head.value == value:
        return head
    p = q = head
    while q.next is not None:
        if q.value == value:
            p.next = q.next
            del q
            node = LinkedNode(value)
            node.next = head
            head = node
            return head
        p = q
        q = q.next
    length = len_of_linked_nodes(head)
    if length < cache_size:
        p.next = LinkedNode(value)
    else:
        p.next = None
        del q
        node = LinkedNode(value)
        node.next = head
        head = node
    return head


if __name__ == '__main__':
    size = 5
    head = init_linked_nodes(size)
    head = lru_by_linked_node(head, 15)
    while head is not None:
        print (head.value, head.next)
        head = head.next
