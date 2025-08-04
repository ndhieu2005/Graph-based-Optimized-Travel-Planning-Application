Toàn bộ mã nguồn được lập trình và chạy trên IDE Spyder, dữ liệu được lưu trên SQL server.

* Cài đặt CSDL locations_db: Toàn bộ file sử dụng dưới đây nằm trong folder locations_database.
B1: Kết nối với server cá nhân trên máy tính, tạo database mới tên là locations_db.
B2: Mở file create_tables.sql, execute để chạy lệnh tạo bảng.
B3: Import dữ liệu từ file CSV location và costs.
	Chuột phải vào database → chọn Tasks → Import Data...

	Chọn nguồn dữ liệu:
	Data source: Flat File Source
	File name: duyệt tới file .csv
	File format: chọn dấu phân cách là Comma

	Chọn đích:
	Destination: SQL Server Native Client
	Nhập thông tin server, chọn database (locations_db)

	Chọn bảng đích:
	Tạo bảng mới hoặc chọn bảng có sẵn
	Nhấn Next, rồi Finish để chạy

*Chạy mã nguồn kiểm thử: 
B1: Mở IDE Spyder, chọn Projects -> New Project... -> Existing directory -> Mục Location chọn folder source_code -> Create.
B2: Mở chương trình Process_data.py, tại hàm get_data chỉnh sửa SERVER theo tên server đã cài đặt CSDL locations_db trước đó. Ấn tổ hợp phím Ctrl+S để lưu cập nhật.
B3: Mở chương trình GUI.py, chạy chương trình rồi kiểm thử.
