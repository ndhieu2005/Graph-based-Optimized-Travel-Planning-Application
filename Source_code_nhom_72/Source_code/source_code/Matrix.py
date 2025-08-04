# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 00:16:05 2025

@author: hoang an
"""

class matrix:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]
        
    def size(self, key):
        if key == 'row':
            return self._rows
        elif key == 'col':
            return self._cols
        else:
            raise KeyError(f"key '{key}' not valid")
        
    def search(self,x):
        for i in range(self._rows):
            for j in range(self._cols):
                if self.data[i][j] == x:
                    return (i,j)
        return None

    def get_value(self, row, col):
        if 0 <= row < self._rows and 0 <= col < self._cols:
            return self.data[row][col]
        else:
            raise IndexError("Index out of bounds")

    def insert(self,row,col,value):
        if (0 <= row < self._rows) and (0 <= col < self._cols):
            self.data[row][col] = value
        else:
            raise IndexError("Index out of bounds")
        
    def delete(self,row,col):
        if (0 <= row < self._rows) and (0 <= col < self._cols):
            self.data[row][col] = 0
        else:
            raise IndexError("Index out of bounds")