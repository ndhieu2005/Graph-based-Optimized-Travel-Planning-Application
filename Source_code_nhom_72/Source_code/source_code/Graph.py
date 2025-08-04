# -*- coding: utf-8 -*-
"""
Created on Fri May 30 11:11:41 2025

@author: hoang an
"""

class Dict:
    """A Dictionary ADT with a linked-item design, where each item consists of a key-value pair."""
    class Item:
        def __init__(self, key, value, next_item):
            self.key = key
            self.value = value
            self.next = next_item
        
    def __init__(self):
        self._head = None
        self._size = 0
        
    def size(self):
        """Return the number of items"""
        return self._size
    
    def key_check(self, key):
        """Check if a key exists return that key-value item, else return None."""
        current = self._head
        while current != None:
            if current.key == key:
                return current
            current = current.next
        return None
        
    def insert(self, key, value):
        """Add or update key-value pair"""
        tmp = self.key_check(key)
        if tmp != None:
            tmp.value = value
            return f"Key '{key}' has been updated with a new value '{value}'."
        else:
            tmp = self._head
            self._head = self.Item(key, value, tmp)
            self._size += 1
            return f"Key '{key}' has been added with value '{value}'."
    
    def remove(self, key):
        """Remove an item with key."""
        tmp = self.key_check(key)
        if tmp != None:
            tmp_2 = tmp.next
            if tmp_2 == None:
                tmp = None
            else:
                tmp.key = tmp_2.key
                tmp.value = tmp_2.value
                tmp.next = tmp_2.next
            self._size -= 1
            return f"Item with key '{key}' has been removed."
        else:
            raise KeyError(f"Key: '{key}' not found.")
        
    def lookup(self, key):
        """Retrieve the value for a key."""
        tmp = self.key_check(key)
        if tmp != None:
            return tmp.value
        else:
            raise KeyError(f"Key '{key}' not found.")
            
    def get_values(self):
        result = []
        current = self._head
        while current != None:
            result.append(current.value)
            current = current.next
        return result

class Graph:
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.neighbors = Dict()
            
    def __init__(self):
        self._names = []
        self._nodes = Dict()
        
    def insert_node(self, name, data=None):
        """Add or update a node with it's data."""
        tmp = self.Node(data)
        self._nodes.insert(key=name, value=tmp)
        if name not in self._names:
            self._names.append(name)

    def get_node(self, name):
        """Return a node depend on it's name."""
        return self._nodes.lookup(name)
    
    def show_nodes(self):
        """Print all nodes' names."""
        for i in range(len(self._names)):
            print(f'{self._names[i]} | ', end='')
    
    def insert_edge(self, u, v, weight=None):
        """Add or update an edge with weight using its endpoints's name."""
        if (u in self._names) and (v in self._names):
            self.get_node(u).neighbors.insert(key=v, value=weight)
            self.get_node(v).neighbors.insert(key=u, value=weight)
        else:
            raise ValueError(f"Node '{u}' or '{v}' does not exist.")
            

            