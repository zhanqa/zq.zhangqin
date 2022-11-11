# 客户机代码
import socket
import os
def sendfile(s):
	str1=s.recv(1024)
	filename=str1.decode('utf-8')
	print('The service requests my file:',filename)
	if os.path.exists(filename):
		print('I have %s,begin to download!'% filename)
		s.send(b'yes')
		s.recv(1024)
		size=1024
		with open(filename,'rb') as f:
			while True:
				data=f.read(size)
				s.send(data)
				if len(data)<size:
					break
		print('%s is download successfully!' %filename)
	else:
		print('Sorry,I have no %s' % filename)
		s.send(b'no')
	s.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 4488))
sendfile(s)





