import tkinter as tk
from tkinter import messagebox
import Graph
import Matrix
import TSP
import Process_data
def GUI():
    # Hàm xử lý khi người dùng xác nhận lựa chọn
    def on_confirm():
        #lấy dãy đỉnh từ người dùng nhập vào
        raw_vertices = entry_vertices.get().strip()
        if not raw_vertices:
            messagebox.showerror("Lỗi", "Vui lòng nhập dãy đỉnh.")
            return
        try: # chuyển đổi dãy đỉnh thành danh sách các số nguyên
            vertices_list = [int(x.strip()) for x in raw_vertices.split(',') if x.strip() != '']
        except ValueError:
            messagebox.showerror("Lỗi", "Dãy đỉnh phải là các số nguyên cách nhau bằng dấu phẩy.")
            return
        #Gán vertices_list vào Graph
        locations = [int(i) for i in vertices_list]  # Chuyển đổi thành chuỗi
        optimize_choice = var_opt.get()
        if optimize_choice == 1:
            m = Process_data.get_adj_matrix(locations, norm=None)  # Lấy ma trận kề từ dữ liệu
        elif optimize_choice == 2:
            m = Process_data.get_adj_matrix(locations, norm='distance')
        elif optimize_choice == 3:
            m = Process_data.get_adj_matrix(locations, norm='time')
        elif optimize_choice == 4:
            m = Process_data.get_adj_matrix(locations, norm='price')
        else:
            messagebox.showerror("Lỗi", "Chưa chọn lựa chọn tối ưu.")
            return
        mintour,tour =  TSP.tsp(m=m, S=0, locations=locations)
        result_text = f"Dãy đỉnh: {vertices_list}\nTiêu chí tối ưu:{optimize_choice}\nMintour: {mintour}\nLộ trình: {' -> '.join(str(x) for x in tour)}"
        result_label.config(text=result_text)
        
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("TSP - Traveling Salesman Problem GUI")
    root.geometry("1200x800")
    
    # Label và entry nhập dãy đỉnh
    Label1 = tk.Label(root,text = "Nhập dãy thành phố(ID từ 1 đến 100,cách nhau bằng dấu phẩy):")
    Label1.pack(pady=(10,1))
    
    entry_vertices = tk.Entry(root, width=50)
    entry_vertices.pack(pady=(0,15))
    
    # Label phần chọn tiêu chí tối ưu
    Label2 = tk.Label(root, text="Chọn tiêu chí tối ưu:")
    Label2.pack(pady=(0,15))
    
    # Biến lưu lựa chọn tiêu chí dưới dạng số 1-4
    var_opt = tk.IntVar(value=1)  # Mặc định chọn tiêu chí 1
    
    # Các lựa chọn tiêu chí tối ưu, giá trị tương ứng 1-4
    options = [
        ("Tiêu chí 1: Tối ưu cả 3 tiêu chí", 1),
        ("Tiêu chí 2: Quãng đường ngắn nhất", 2),
        ("Tiêu chí 3: Thời gian di chuyển ngắn nhất", 3),
        ("Tiêu chí 4: Ngân sách thấp nhất", 4)
    ]
    
    # Tạo radio buttons cho các tiêu chí tối ưu
    for text, value in options:
        radio = tk.Radiobutton(root, text=text, variable=var_opt, value=value)
        radio.pack(anchor=tk.W)
    
    # Nút xác nhận
    btn_confirm = tk.Button(root, text="Xác nhận", command=on_confirm)
    btn_confirm.pack(pady=10)
    
    # Label để hiển thị kết quả
    result_label = tk.Label(root, text="Kết quả sẽ hiển thị ở đây", font=("Arial", 12),justify="left")
    result_label.pack(pady=10)
    
    # Chạy vòng lặp giao diện
    root.mainloop()
    
def main():
    GUI()
    
if __name__ == "__main__":
    main()