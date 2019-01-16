
# Web site extraction
url_list = []
def file_proc(filename):
	with open(filename, 'r') as f:
		for i in f.readlines():
			i = i.split('/')[2]
			url_list.append(i.strip())

	return url_list

