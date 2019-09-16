# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
算法思想：
1 hash(object)%N, hash_ring,each node == key,
2 Hash(node_n)=key_n+Hash(object_n)=key_n
3 add/remove node,顺时针将对应的key放到next_node
3 虚拟节点映射VirtualNodeHash(node_n#1) = node_n_1, VirtualNodeHash(node_n#2) = node_n_2, 
  Hash(node_n_1)=key_x, Hash(node_n_2)=key_y
"""