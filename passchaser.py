# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import os, sys
import urllib.request
import io
import bs4 as bs
import ssl



	
def logo():
	logo = '''\033[1;31m
 ____               _   _             _   
██████╗  █████╗ ███████╗███████╗ ██████╗██╗  ██╗ █████╗ ███████╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██╔══██╗██╔════╝██╔════╝██╔══██╗
██████╔╝███████║███████╗███████╗██║     ███████║███████║███████╗█████╗  ██████╔╝
██╔═══╝ ██╔══██║╚════██║╚════██║██║     ██╔══██║██╔══██║╚════██║██╔══╝  ██╔══██╗
██║     ██║  ██║███████║███████║╚██████╗██║  ██║██║  ██║███████║███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
           \033[1;32m  	 ***523 vendors, 2084 passwords*** 
                            Author: PriYank
                      Twitter: @priyankvadaliya
 Description: This tool is to search default credentials for routers, network devices, web applications and more. 
 \033[1;32m\033[1;m'''
	return logo

OPTIONS = '''\033[1;33m
1. List supported vendors
2. Search Default Password
3. Exit
\033[1;33m'''

try:
	_create_unverified_https_context = ssl._create_unverified_https_context
except AttributeError:
	pass

else:
	ssl._create_default_https_context = _create_unverified_https_context

def opt():
	while True:
		try:
			choice = str(input('\n \033[1;34m [?] \033[1;m Do You Went To Continue? \n'))
			if choice[0] == 'y':
				return
			if choice[0] == 'n':
				sys.exit(0)
				break
		except ValueError:
			sys.exit(0)

def  checkInternetConnection():
	try:
		urllib.request.urlopen('https://cirt.net/')
	except:
		print('\033[1;31m[!] \033 No internet connection ...Please connect to the Internet')
	else:
		print('\033[1;32m[+] Checking Internet connection... \033[1;m')

def formatTable(table):
	text=''
	rows=table.find_all('tr')
	text+='\n\033[1;31m%s\n\033[1;31m' % rows[0].text

	for row in rows[1:]:
		data = row.find_all('td')
		text += '\033[1;32m%s:\033[1;32m \033[1;33m%s\n\033[1;33m' % ((data[0].text),data[1].text)

	return text


def cmd_vendorSearch():
	vendor =input("\nEnter Vendor Name : ").lower()
	urlenc = urllib.parse.quote(vendor)
	url = "http://cirt.net/passwords?vendor=" + urlenc
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	soup = bs.BeautifulSoup(response,"html.parser")

	for links in soup.find_all('table'):
		print(formatTable(links))

def cmd_openfile():
	path = './vendors.txt'
	vendors_file = open(path,'r')
	vendors = vendors_file.read()
	print(vendors)

cmds = {
	
		"1" : cmd_openfile,
		"2" : cmd_vendorSearch,
		"3" : lambda: sys.exit(0)
}

def main():
	print(logo())
	checkInternetConnection()
	try:
		while True:
			choice = input("\n\n%s" % OPTIONS)
			if choice not in cmds:
				print('\033[1;31m[!] Invalid Choice')
				continue
			cmds.get(choice)()
	except KeyboardInterrupt:
		print('\033[1;31m[!] \033 Ctrl + c detected\n [!] Exiting')
		sys.exit(0)
	except EOFError:
		print('\033[1;31m[!] \033 Ctrl + D detected \n [!] Exiting')
		sys.exit(0)

if __name__ == "__main__":
	main()


	
                                                                                

