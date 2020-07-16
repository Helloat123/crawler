import requests
url="http://zt.zjzs.net/xk2020/10001.html"
head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

cook={"Cookie":'BAIDUID=FE0F97F1FC37C47792091A2523CD945F:FG=1; HMACCOUNT=CC6D0E280C842123'}
try:
	r=requests.get(url,cookies=cook,headers=head,timeout=5)
	r.raise_for_status()	#如果状态码不是200，产生异常
	r.encoding='utf-8-sig'		#字符编码格式改成 utf-8
	print("good")
except Exception as e:
	print(str(e))
	#异常处理
	print("get html text error")
