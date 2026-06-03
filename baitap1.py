delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]

# Thêm vào cuối danh sách
delivery_orders_append = delivery_orders.append("GE004")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
delivery_orders_insert = delivery_orders.insert(0, "GE000")

# Sửa đơn hàng GE002 thành GE002-UPDATE
delivery_orders[2] = "GE002-UPDATE"

# Xóa đơn hàng bị hủy
delivery_orders_remove = delivery_orders.remove("GE003-CANCEL")

# Lấy đơn hàng để bàn giao cho tài xế khác
transferred_order = delivery_orders.pop(3)

print(f"Danh sách đơn hàng còn lại: {delivery_orders}")
print(f"Đơn hàng đã được bàn giao cho tài xế: {transferred_order}")