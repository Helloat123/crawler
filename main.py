import requests,re
import time
import random
from bs4 import BeautifulSoup
path="d://programing//PY//crawlerdata//"
head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
def getHTMLText(url):
	try:
		r=requests.get(url,headers=head,timeout=30)
		r.raise_for_status()	#如果状态码不是200，产生异常
		r.encoding='utf-8-sig'		#字符编码格式改成 utf-8
		return r.text
	except:
		#异常处理
		return "get html text error"

def single(url,inde):
	try:
		# print(url)
		htmltext=getHTMLText(url)
	except:
		throw("Nothing here!")


	try:
		soup=BeautifulSoup(htmltext,"html.parser")
		#con=soup.find_all('',class_="")
		#for i in range(len(con)):
		#	print(con[i].text)
		

	except:
		print("Failed soup")
	
	try:
		htm=open(path+"htmdata//"+"htmdata"+str(inde)+".txt",'w+')
		htm.write(str(soup))
		htm.close()
		print("Got it!")
	except Exception as e:
		print(str(e))



#main part
log=open(path+"log.txt",'w+')
# for i in range(10001,91000):
for i in range(10001,10002):
	try:
		print(i)
		single("http://zt.zjzs.net/xk2020/"+str(i)+".html",i)
		time.sleep(random.randint(5,10))
		log.write("http://zt.zjzs.net/xk2020/"+str(i)+".html\n")
	except:
		log.write("There's nothing in",i)
log.close()