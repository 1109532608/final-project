#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next

class CompleteBinaryTree:
    def __init__(self, root=None, last=None):
        self.root = root
        self.size = 0
    
    def get_parent_index(self, i):
        return (i-1) // 2
    
    def get_left_child_index(self, i):
        return (2*i) + 1
    
    def get_right_child_index(self, i):
        return (2*i) + 2
    
    def insert(self, key):
        new_node = Node(key) 
        if self.size == 0:
            self.root = new_node
        else:
            curr = self.root
            i = 0
            while curr is not None:
                prev = curr
                curr = curr.next
                i += 1
                if i == self.size:
                    break
            prev.next = new_node        
        self.size += 1
        
    def delMin(self):
        if self.size == 0:
            raise ValueError('Tree is empty')
        min_node = self.root
        min_prev = None
        curr = self.root.next
        prev = self.root
        while curr is not None:
            if curr.key < min_node.key:
                min_node = curr
                min_prev = prev
            prev = curr
            curr = curr.next
        if min_prev is None:
            self.root = self.root.next
        else:
            min_prev.next = min_node.next
        self.size -= 1
        return min_node.key
        


# In[2]:


import time
import matplotlib.pyplot as plt
heap = CompleteBinaryTree()
insert_times = []
del_min_times = []
for i in range(1, 1000):
    start_time = time.perf_counter()
    heap.insert(i)
    end_time = time.perf_counter()
    insert_times.append(end_time - start_time)
    start_time = time.perf_counter()
    heap.delMin()
    end_time = time.perf_counter()
    del_min_times.append(end_time - start_time)
plt.plot(insert_times, label='insert')
plt.plot(del_min_times, label='delMin')
plt.legend()
plt.show()

