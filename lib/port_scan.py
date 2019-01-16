import lib.file_processing as fp 
import socket
import threading
from datetime import datetime

lock = threading.Lock()
threads = []
success_list = []
url_list = []
threads_num = ''
# Extract IP

def Get_ip(url):
	try:
		return socket.gethostbyname(url)
	except socket.error as e:
		print('[+] %s: %s' %(url,e))
# Port scan

def Port_Scan(ip,port):
	try:
		s = socket.socket()
		s.settimeout(0.1)
		s.connect((ip,port))
		lock.acquire()
		openstr = '[+] PORT: ' + str(port) + ' OPEN'
		success_list.append(str(port))
		print(openstr)
		lock.release()
		s.close()
	except:
		pass
# Start scan and save

def scan(url,threads_num):
	ip = Get_ip(url)
	print('[*] The target is ' + ip + ' The threads number of threads is ' + threads_num)
	for n in range(1,int(threads_num)+1):
		for port in range((n-1)*(66000//int(threads_num)),n*(66000//int(threads_num))):
			t = threading.Thread(target=Port_Scan,args=(ip,port))
			threads.append(t)
			t.start()
		for t in threads:
			t.join()
	filename = 'output/Port/' + datetime.now().date().isoformat() + ' ' + url +'.txt'
	with open(filename, 'a') as f:
		for i in success_list:
			f.write(ip + ':'+ i + '\n')
	print('[*] The scan is completed and the results are saved to ' + filename)
# Set threads number

def main():
	url_list = fp.url_list
	num = threads_num
	for url in url_list:
		scan(url,threads_num)
