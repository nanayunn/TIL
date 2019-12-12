import webbrowser

# webbrowser.open('www.google.co.kr')
# webbrowser.open_new('www.naver.com')
# webbrowser.open_new_tab('www.daum.net')

import requests
# res = requests.get('http://naver.com')
# print(res)
# print(res.text)


from bs4 import BeautifulSoup
#KOSPI_now
# https://finance.naver.com/sise/

#코스피 정보 빼오기
url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
soup=BeautifulSoup(response, 'html.parser')
kospi = soup.select_one('#KOSPI_now')
print(kospi.text)

#exchangeList > li.on > a.head.usd > div > span.value
#https://finance.naver.com/marketindex/

#환율정보 빼오기
url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
soup=BeautifulSoup(response, 'html.parser')
exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
print(exchange.text)

from datetime import datetime

# https://www.naver.com/
url = 'https://www.naver.com/'
response = requests.get(url).text
soup=BeautifulSoup(response, 'html.parser')
now = datetime.now()
search = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li .ah_k')

print(f'{now}기준 실시간 검색어')

# for name in search:
#     print(name.text)

# enumerate:열거해주는 함수
# 반복되는 순서에 숫자를 붙여주는 것.
for i, name in enumerate(search):
    print(f'{i+1}위 : {name.text}')