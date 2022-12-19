import socket

ip = '127.0.0.1'
port = 5500

itemtemplate = \
		"SET RIBBON ON\r\n" + \
		"SIZE 74 mm,45 mm\r\n" + \
		"GAP 4 mm,0\r\n" + \
		"CLS\r\n" + \
		"DIRECTION 1\r\n" + \
		"TEXT 250,5,\"0\",0,15,15,\"ООО ''ММВЗ''""\"\r\n" + \
		f"TEXT 20,450,\"0\",0,6,6,\"Линия № 3""\"\r\n" + \
		f"TEXT 750,450,\"0\",0,6,6,\"Стол №1""\"\r\n" + \
		"PRINT 1\r\n"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip, port))
    s.sendall(itemtemplate.encode())