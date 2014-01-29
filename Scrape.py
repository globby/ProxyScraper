import json
import urllib2
import time
import re
from bs4 import BeautifulSoup

fname = time.strftime("%H.%M.%S %d.%m.%Y.txt",time.localtime())

def scrape(db):
	url = "http://www.ip-adress.com/proxy_list/?k=time&d=desc"
	req = urllib2.Request(url,'')
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.5) Gecko/2008120122 Firefox/3.0.5')
	data = urllib2.urlopen(req).read()
	soup = BeautifulSoup(data)
	ips = soup.find_all("tr",class_=re.compile("(even|odd)"))
	for ip in ips:
		i = {
		"ip":ip.contents[1].string,
		"type":ip.contents[3].string,
		"country":ip.contents[5].img.string.strip()
		}
		if i not in db:
			db.append(i)
			print i

if __name__ == "__main__":
	db = []
	while True:
		scrape(db)
		f = open(fname,'w')
		f.write(json.dumps(db))
		f.close()
		time.sleep(5)