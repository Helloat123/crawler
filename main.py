import requests
from bs4 import BeautifulSoup
path="d://programing//PY//crawlerdata//"
def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()	#如果状态码不是200，产生异常
		r.encoding='utf-8-sig'		#字符编码格式改成 utf-8
		return r.text
	except:
		#异常处理
		return "get html text error"

def single(url):
	try:
		# print(url)
		htmltext=getHTMLText(url)
	except:
		throw("Nothing here!")

	return

	try:
		soup=BeautifulSoup(htmltext,"html.parser")
		con=soup.find_all('',class_="")
		#for i in range(len(con)):
		#	print(con[i].text)
		print(soup)
	except:
		print("Failed soup")
	
	try:
		htm=open(path+"htmdata.txt",'w+')
		htm.write(htmltext)
		htm.close()
		print("Got it!")
	except Exception as e:
		print(str(e))



#main part

log=open(path+"log.txt",'w+')
# for i in range(10001,91000):
for i in range(10001,10005):
	try:
		print(i)
		single("http://zt.zjzs.net/xk2020/"+str(i)+".html")
		# log.write("http://zt.zjzs.net/xk2020/"+str(i)+".html\n")
	except:
		log.write("There's nothing in",i)
log.close()
	