from socket import *

serverPort = 12000

# Tạo socket UDP: sử dụng IPv4 (AF_INET) và UDP (SOCK_DGRAM)
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Gắn socket vào địa chỉ và cổng xác định
serverSocket.bind(('', serverPort))
print('The server is ready to receive')

while True:
    # Nhận dữ liệu từ client, độ dài tối đa của dữ liệu là 2048 byte
    message, clientAddress = serverSocket.recvfrom(2048)
    
    # Giải mã message từ byte sang chuỗi và chuyển sang chữ in hoa
    modifiedMessage = message.decode().upper()
    
    # In ra message ban đầu nhận từ client
    print(f"Received message : {clientAddress}: {message.decode()}")
    
    # In ra message đã chỉnh sửa để gửi lại
    print(f"Result : {modifiedMessage}")
    
    # Gửi lại message đã chuyển thành chữ in hoa cho client
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
