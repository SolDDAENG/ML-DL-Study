import urllib.request
url = 'https://www.google.co.kr'

mem = urllib.request.urlopen(url).read()
print(mem.decode('euc-kr'))