from socket import *

serverPort = 12000

# Tạo socket TCP (SOCK_STREAM) sử dụng IPv4 (AF_INET)
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)  # Lắng nghe tối đa 1 kết nối tại 1 thời điểm
print('The server is ready to receive')

while True:
    # Chấp nhận kết nối từ client
    connectionSocket, clientAddress = serverSocket.accept()
    print(f"Connection established with {clientAddress}")

    # Vòng lặp để nhận và xử lý nhiều tin nhắn từ cùng một client
    while True:
        # Nhận dữ liệu từ client, tối đa 1024 byte
        message = connectionSocket.recv(1024).decode()

        if not message or message.lower() == 'exit':
            print(f"Client {clientAddress} đã ngắt kết nối.")
            break

        # In ra message nhận được từ client
        print(f"Received message: {message}")

        # Chuyển đổi message sang chữ in hoa
        modifiedMessage = message.upper()
        print(f"Result: {modifiedMessage}")

        # Gửi lại dữ liệu đã chỉnh sửa cho client
        connectionSocket.send(modifiedMessage.encode())

    # Đóng kết nối với client
    connectionSocket.close()
    print(f"Connection with {clientAddress} closed\n")
