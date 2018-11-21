import urllib2

url = "https://www.baidu.com/"
# 简单爬虫
print('method one')
response1 = urllib2.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print('method two')
request = urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib2.urlopen(request)
print(response2.getcode())
print(len(response2.read()))

print('method three')
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print(response3.getcode())
print(cj)
print(response3.read())
