import re,sys
path=sys.argv[1]

inp=open(path,'r')
s=inp.read()

pos=s.find('学校名称：')
if pos==-1: print("ERROR!!")
i=pos+5
cnt=0
ss=''
while s[i]!=' ':
	cnt=cnt+1
	ss=ss+s[i]
	i=i+1
name=ss

pos=s.find('学校代码：')
if pos==-1: print("ERROR!!")
i=pos+5
cnt=0
ss=''
while s[i]!=' ':
	cnt=cnt+1
	ss=ss+s[i]
	i=i+1
index=ss

while 