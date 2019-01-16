import sys,getopt
import lib.file_processing as fp
import lib.port_scan as ps
# Define banner information

def usage():
	banner = '''


 $$$$$$\                                 $$\                               $$\ $$\                       $$\     $$\                     
$$  __$$\                                $$ |                              $$ |$$ |                      $$ |    \__|                    
$$ /  $$ | $$$$$$$\  $$$$$$$\  $$$$$$\ $$$$$$\          $$$$$$$\  $$$$$$\  $$ |$$ | $$$$$$\   $$$$$$$\ $$$$$$\   $$\  $$$$$$\  $$$$$$$\  
$$$$$$$$ |$$  _____|$$  _____|$$  __$$\\_$$  _|$$$$$$\ $$  _____|$$  __$$\ $$ |$$ |$$  __$$\ $$  _____|\_$$  _|  $$ |$$  __$$\ $$  __$$\ 
$$  __$$ |\$$$$$$\  \$$$$$$\  $$$$$$$$ | $$ |  \______|$$ /      $$ /  $$ |$$ |$$ |$$$$$$$$ |$$ /        $$ |    $$ |$$ /  $$ |$$ |  $$ |
$$ |  $$ | \____$$\  \____$$\ $$   ____| $$ |$$\       $$ |      $$ |  $$ |$$ |$$ |$$   ____|$$ |        $$ |$$\ $$ |$$ |  $$ |$$ |  $$ |
$$ |  $$ |$$$$$$$  |$$$$$$$  |\$$$$$$$\  \$$$$  |      \$$$$$$$\ \$$$$$$  |$$ |$$ |\$$$$$$$\ \$$$$$$$\   \$$$$  |$$ |\$$$$$$  |$$ |  $$ |
\__|  \__|\_______/ \_______/  \_______|  \____/        \_______| \______/ \__|\__| \_______| \_______|   \____/ \__| \______/ \__|  \__|



                                                                                                                                         
                                        		Author:Echocipher

                                        	   A tool for asset collection
'''
	print(banner)
	print('[*] main.py -h -View Help Documents')
	print('[*] main.py -u target -Setting a single goal')
	print('[*] main.py -r file -Setting multiple goals')
	print('[*] main.py -s port|subdomain|catalog|all -Selection Function Module')
	print('[*] main.py -t number -Set thread')

def main():
# Processing command line parameters

	if not len(sys.argv[1:]):
		usage()
	try:
		opts,args = getopt.getopt(sys.argv[1:],"hu:r:s:t:")
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for o,a in opts:
		# help
		if o == '-h':
			usage() 
		# target
		elif o == '-u':
			fp.url_list.append(a.split('/')[2])
		# target file
		elif o == '-r':
			fp.file_proc(a)
		elif o == '-t':
			ps.threads_num = a
		elif o == '-s':
			if a == 'port':
				ps.main()
			elif a == 'subdomain':
				print('subdomain')
			elif a == 'catalog':
				print('catalog')
			elif a == 'all':
				print('all')
			else:
				print('[*] please input port|subdomain|catalog|all')



if __name__ == '__main__':
	main()
