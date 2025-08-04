# -*- coding: utf-8 -*-
"""
Created on Sat May 31 01:34:07 2025

@author: hoang an
"""

import pyodbc

def get_data(locations):
    """Lấy dữ liệu từ database khớp với các địa điểm trong locations"""
    # Danh sách đỉnh cần lọc
    id_list = locations
    
    """Kết nối đến cơ sở dữ liệu"""
    """Lưu ý: Đổi tên SERVER thành đúng tên server chứa CSDL"""
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=MONKEYMIND;'
        'DATABASE=locations_db;'
        'Trusted_Connection=yes;'
        'Encrypt=no;'
        'TrustServerCertificate=yes;'
    )
    cursor = conn.cursor()
    
    """Thực hiện câu lệnh truy vấn"""
    # Số dấu hỏi tương ứng số phần tử
    placeholders = ','.join('?' for _ in id_list)
    
    query = f'''
    SELECT *
    FROM costs
    WHERE Vertex_1 IN ({placeholders})
      AND Vertex_2 IN ({placeholders})
    '''
    
    # Truyền 2 lần id_list vì dùng cho cả Vertex_1 và Vertex_2
    params = id_list + id_list
    cursor.execute(query, params)
    
    """Lấy dữ liệu đã được truy vấn để lưu vào danh sách lồng"""
    data = []
    results = cursor.fetchall()
    for row in results:
        data.append(row)
    
    """Ngắt kết nối với database"""
    cursor.close()
    
    return data

def suit_norm(data, norm=None):
    """Tính toán cost phụ thuộc vào norm"""
    import math
    result_data = []

    if norm == 'distance':
        result_data = [ [row[0],row[1],row[3]] for row in data]
    elif norm == 'time':
        result_data = [ [row[0],row[1],row[4]] for row in data]
    elif norm == 'price':
        result_data = [ [row[0],row[1],row[5]] for row in data]
    elif norm == None:
        for row in data:
            cost = math.sqrt(row[3] ** 2 + row[4] ** 2 + row[5] ** 2)
            result_data.append( [row[0],row[1],cost] )
    else:
        raise ValueError(f"Unsupported norm: {norm}")
    
    return result_data

def filter_data(data):
    """Lọc dữ liệu để lấy cách đi có cost thấp nhất"""
    result = {}
    for sublist in data:
        key = (sublist[0], sublist[1])
        value = sublist[2]
        if key not in result or value < result[key][2]:
            result[key] = sublist
    
    # Kết quả dưới dạng list các sub-list đã lọc
    filtered_data = list(result.values())
    return filtered_data

def get_adj_matrix(locations, norm):
    import Graph
    
    """lấy và xử lý dữ liệu từ database"""
    data = get_data(locations)
    data = suit_norm(data, norm)
    data = filter_data(data)
    
    G = Graph.Graph()
    for i in locations:
        G.insert_node(name = i, data = None)
    
    for i in data:
        G.insert_edge(i[0], i[1], i[2])
    
    """Sinh ma trận kề, độ phức tạp O(4n^2) - n là số phần tử trong locations"""
    import Matrix
    adj_matrix = Matrix.matrix(len(locations), len(locations))
    for i in range(len(locations)):
        tmp_node = G.get_node(locations[i])
        tmp = tmp_node.neighbors.get_values()
        tmp.reverse()
        for j in range(len(locations)):
            if j == i:
                adj_matrix.insert(i, j, float('inf'))
            elif j < i:
                adj_matrix.insert(i, j, tmp[j])
            else:
                adj_matrix.insert(i, j, tmp[j-1])

    return adj_matrix
            