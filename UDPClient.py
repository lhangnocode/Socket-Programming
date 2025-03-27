from socket import *

serverName = '172.20.10.10'

serverPort = 12000

# Tạo socket UDP: sử dụng IPv4 (AF_INET) và UDP (SOCK_DGRAM)
clientSocket = socket(AF_INET, SOCK_DGRAM)

print("Kết nối tới server thành công. Nhập 'exit' để thoát.")

# Vòng lặp cho phép gửi nhiều tin nhắn cho đến khi gõ 'exit'
while True:
    message = input('Input lowercase sentence: ')

    if message.lower() == 'exit':
        print('Đang đóng kết nối...')
        break

    # Gửi message đã nhập tới server với địa chỉ và cổng xác định
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    # Nhận dữ liệu từ server, tối đa 2048 byte
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

    # In ra message đã chỉnh sửa (chuyển thành chữ hoa)
    print(f"Result: {modifiedMessage.decode()}")

# Đóng socket client sau khi hoàn tất giao tiếp
clientSocket.close()
print('Kết nối đã được đóng.')
