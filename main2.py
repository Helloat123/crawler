import re
def printinto(ss)
	res=re.search('<div style=" float:left;width:50%;">.*</div> <div style=" float:left;width:50%;">',ss)
	resstr=res.group(0)
	reslog.write(resstr[36,-43]+'\n')

	res1=re.findall(ss,)