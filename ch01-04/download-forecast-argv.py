# !/usr/bin.env python3

# 라이브러리를 읽어 들입니다. --- (1)
import sys # sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.
import urllib.request as req
import urllib.parse as parse

# 명령줄 매개변수 추출 --- (2)
if len(sys.argv) <= 1:  # 명령 행에서 인수 전달하기 - sys.argv
    print("USAGE : download-forecast-argv <Region Number>")
    sys.exit()
regionNumber = sys.argv[1]

# 매개변수를 URL 인코딩합니다. --- (3)
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stdId : regionNumber'
}
params = parse.urlencode(values)
url = API + "?" + params
print('url=', url)

# 다운로드합니다. --- (4)
data = req.urlopen(url).read()
text = data.decode('utf-8')
print(text)