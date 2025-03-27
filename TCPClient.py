from socket import *

# Địa chỉ server (localhost hoặc IP)
serverName = '172.20.10.10'

serverPort = 12000

# Tạo socket TCP (SOCK_STREAM) cho client
clientSocket = socket(AF_INET, SOCK_STREAM)

# Kết nối tới server thông qua địa chỉ và cổng
clientSocket.connect((serverName, serverPort))

print("Kết nối tới server thành công. Nhập 'exit' để thoát.")

while True:
    sentence = input('Input lowercase sentence: ')
    
    if sentence.lower() == 'exit':
        print('Đang đóng kết nối...')
        break

    # Gửi message đã nhập cho server
    clientSocket.send(sentence.encode())

    # Nhận dữ liệu từ server (tối đa 1024 byte)
    modifiedSentence = clientSocket.recv(1024)

    # In kết quả từ server
    print('From Server:', modifiedSentence.decode())

# Đóng kết nối với server
clientSocket.close()
print('Kết nối đã được đóng.')
