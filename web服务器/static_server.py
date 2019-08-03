#conding=utf-8

import socket
import multiprocessing

def handle_socket(client_socket):
    """接受客户端的请求"""
    request_data = client_socket.recv(1024)
    print("request_data:", request_data)

    #构建客户端的http报文，状态行和首部行
    response_start_list = "HTTP/1.1 200 ok\r\n"
    response_header = "Server: My server\r\n"
    response_body = "are you ok?"
    response = response_start_list + response_header + "\r\n" + response_body
    print("response data:", response)
    #发送客户端http报文
    client_socket.send(bytes(response, "utf-8"))
    #关闭客户端
    client_socket.close()


if __name__ == "__main__":
        #创建server套接字
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("", 7787))
        server_socket.listen(124)

        while True:
            client_socket, client_address = server_socket.accept()
            print("[%s, %s]用户已经链接上了" % client_address)
            handle_client_process = multiprocessing.Process(target=handle_socket, args=(client_socket,))
            handle_client_process.start()
            client_socket.close()