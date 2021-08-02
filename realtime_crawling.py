from datetime import datetime
from url_list import *
import requests
from bs4 import BeautifulSoup

data = {}

def realtime_crawling(url):
    req = requests.get(url)
    # html 소스 가져오기
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    tbody = soup.find('tbody')
    trs = tbody.findAll('tr')

    # 고정된 공지사항 갯수 구하기
    headline_trs = soup.findAll('tr', 'headline')
    fixedNum = len(headline_trs)

    # 고정된 공지사항을 제외한 최신 공지 5개
    trs_5 = trs[fixedNum:fixedNum + 5]
    for tr in trs_5:
        notices = []
        basic_url = 'https://www.sungshin.ac.kr'
        a = tr.find('a')
        # 공지사항 제목
        title = a.find('strong').text.strip()
        # 공지사항 url
        href = basic_url + tr.find('a')['href']
        # 공지사항 날짜
        day = tr.findAll('td')[2].text.strip()

        notices.append(url)
        notices.append(day)
        data[title] = notices

    return data


def entire_realtime_crawling():
    for url in url_list:
        print(url)
        realtime_crawling(url)


# 1시간마다 실행행
if __name__ =='__main__':
    now = datetime.now()
    nowHour = now.hour
    while True:
        now = datetime.now()
        if nowHour != now.hour:
            nowHour = now.hour
            entire_realtime_crawling()
            print(data)

