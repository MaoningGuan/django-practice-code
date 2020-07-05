#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import errno
import threading
import time

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = '''Hello, world! <h1> from the5fire 《Django企业开发实战》</h1> - from {thread_name}'''
response_params = [
    'HTTP/1.0 200 OK',
    'Date: Sun, 07 June 2020 19:08:00 GMT',
    'Content-Type: text/html; charset=utf-8',
    'Content-Length: {length}\r\n',
    body,
]
response = '\r\n'.join(response_params)


def handle_connection(conn, addr):
    print('oh, new conn', conn, addr)
    length = len(threading.enumerate())  # 枚举返回个列表
    print('当前运行的线程数为：%d' % length)
    # time.sleep(60)
    request = b""
    while EOL1 not in request and EOL2 not in request:
        try:
            request += conn.recv(1024)
        except socket.error as e:
            if e.args[0] != errno.EWOULDBLOCK:
                raise
            continue

    print(request)
    current_thread = threading.currentThread()
    current_length = len(body.format(thread_name=current_thread.name).encode())
    # length = len(threading.enumerate())  # 枚举返回个列表
    # print('当前运行的线程数为：%d' % length)
    # print(current_thread.name)
    # print(response.format(thread_name=current_thread.name, length=current_length).encode())
    conn.send(response.format(thread_name=current_thread.name, length=current_length).encode())  # response转为bytes后传输
    conn.close()


def main():
    # socket.AF_INET 用于服务器与服务器之间的网络通信
    # socket.SOCK_STREAM 用于基于TCP的流式socket通信
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口可复用，保证我们每次按Ctrl+C组合键之后，快速重启
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('127.0.0.1', 8000))
    serversocket.listen(10)  # 设置backlog-socket连接最大排队数量
    print(serversocket.getsockname())
    serversocket.setblocking(0)   # 设置socket为非阻塞模式
    try:
        i = 0
        while True:
            try:
                conn, address = serversocket.accept()
            except socket.error as e:
                # print(e.args[0])
                # print(errno.EWOULDBLOCK)
                if e.args[0] != errno.EWOULDBLOCK:
                    raise
                continue
            i += 1
            print(i)
            t = threading.Thread(target=handle_connection, args=(conn, address), name='thread-%s' % i)
            t.start()
    finally:
        serversocket.close()


if __name__ == '__main__':
    main()
    # # 获取本机计算机名称
    # hostname = socket.gethostname()
    # # 获取本机ip
    # ip = socket.gethostbyname(hostname)
    # print(ip)
