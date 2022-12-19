import datetime
import socket
import time
from tkinter import *


code_of_factury = "010000000275" #код предприятия (FSRAR ID)
packaging = "1" #тип упаковки (1 - короб, 2 - паллета, 3 - сборнный короб, 4 - сборный паллет)
line_number = "03" # номер линии
count_of_labels = 20
ip = "127.0.0.1"
port = 5500


def script(value_bar: str, value_text: str) -> bytes:
	itemtemplate = \
		"SET RIBBON ON\r\n" + \
		"SIZE 74 mm,45 mm\r\n" + \
		"GAP 4 mm,0\r\n" + \
		"CLS\r\n" + \
		"DIRECTION 1\r\n" + \
		"TEXT 250,5,\"0\",0,15,15,\"ООО ''ММВЗ''""\"\r\n" + \
		f"TEXT 20,80,\"0\",0,8,8,\"{value_text}""\"\r\n" + \
		f"BARCODE 170,170,\"128\",200,1,0,3,1,\"{value_bar}\"\r\n" + \
		f"TEXT 20,450,\"0\",0,6,6,\"Линия № 3""\"\r\n" + \
		f"TEXT 750,450,\"0\",0,6,6,\"Стол №1""\"\r\n" + \
		"PRINT 1\r\n"
	return itemtemplate.encode()


def code_creating(code_of_factury: str, packaging: str, line_number: str) -> str:
	data = datetime.datetime.now().strftime("%m%d%H%M%S")
	return f"{code_of_factury}{packaging}{line_number}{data}"


def main():
	def clicked():
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			a = Label(window, text="Ошибка запроса. Проверьте сетевые настройки сокета")
			b = Label(window, text="Файл settings.json")
			try:
				s.settimeout(1)
				s.connect((ip, port))

				value_from_file = 0
				res = txt.get()
				a.pack_forget()
				b.pack_forget()
				for i in range(count_of_labels):
					value_from_file += 1
					if value_from_file > 9:
						value_from_file = 0
					time.sleep(0.5)
					s.sendall(script(code_creating(code_of_factury, packaging, line_number) + str(value_from_file), res))
			except TimeoutError:
				a.grid()
				b.grid()



	window = Tk()
	window.attributes("-topmost", True)
	window.title("Печать этикеток")
	w = window.winfo_screenwidth()-400
	h = window.winfo_screenheight()-360
	window.geometry(f'380x250+{w}+{h}')
	lbl = Label(window, text="Название продукта")
	lbl.grid()
	txt = Entry(window, width=60)
	txt.grid()
	btn = Button(window, text=f"Напечатать {count_of_labels} этикеток", command=clicked, height=10, width=20)
	btn.grid()
	window.mainloop()


if __name__ == '__main__':
	main()

