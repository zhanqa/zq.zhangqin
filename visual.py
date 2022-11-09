#在主机上操作
from socket import *
from tkinter import *
import tkinter
def server():
	IP = ''
	PORT = 50000
	BUFLEN = 512
	listenSocket = socket(AF_INET,SOCK_STREAM)
	listenSocket.bind((IP,PORT))
	listenSocket.listen(8)
	print(f'客户端启动成功，在{port}端口等待客户端连接...')
	dataSocket,addr =listenSocket.accept()
	print('接收一个客户端',addr)
	while True:
		receved = dataSocket.recv(BUFLEN)

		if not receved:
			break

		info = receved.decode()
		print(f'收到对方信息：{info}')

		dataSocket.send(f'服务端收到信息:{info[::-1]}'.encode())

	dataSocket.close()
	listenSocket.close()
window =tkinter.Tk()
window.title('serverOperation')
window.geometry('1000x200')

button=tkinter.Button(window,text='主机上操作',bg='#CC33CC', command=lambda : server())
button.pack()

top=mainloop()
