#!/bin/python
#coding:UTF-8
import urlparse, copy, urllib

smscontent='test message'
#path存的是txt文件的路径
path='/root/pythondir/phoneNo.txt'
#初始化lie列表
phoneNo=[]

file = open(path)
while 1:
    lines = file.readlines(1000)
    if not lines:
        break
    for line in lines:
          line=line.replace('\n','').split(",")
          phoneNo.append(line[0])

def url_values_replace(sourceURL,values):
    return [ sourceURL.replace('<inputPhoneNo>',phone) for phone in values ]

sourceURL="http://192.168.10.10:13013/cgi-bin/sendsms?username=tester&password=foobar&to=<inputPhoneNo>&text="+smscontent+"&from=test"

actualURL = url_values_replace(sourceURL, phoneNo)
for pure_url in actualURL:
    sendURL = urllib.urlopen(pure_url)

print sendURL
file.close
sendURL.close()

