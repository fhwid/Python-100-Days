from socket import socket


def main():
    # 1.创建socket对象默认使用IPv4和TCP协议
    client = socket()
    # 2.连接到服务器（需要指定IP地址和端口）
    client.connect(('10.119.147.141', 6789))
    # 3.从服务器接收数据
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == "__main__":
    main()
