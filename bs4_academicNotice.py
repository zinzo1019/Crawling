from urllib import parse

from department_urls import *

import requests
from bs4 import BeautifulSoup

# 공지사항 본문 가져오기
def get_content(url):
    req = requests.get(url)
    # html 소스 가져오기
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    # 공지사항의 제목--------------------------------
    title = soup.find('h2', 'artclViewTitle').text.strip()
    print(title)

    left = soup.find('div', 'left')
    dls = left.findAll('dl')

    # 작성일----------------------------------------
    date = dls[0].find('dd').text.strip()
    # 수정일----------------------------------------
    modification = dls[1].find('dd').text.strip()
    # 작성자----------------------------------------
    writer = dls[2].find('dd').text.strip()
    # 조회수----------------------------------------
    views = dls[3].find('dd').text.strip()
    # print(date + " " + modification + " " + writer + " " + views)

    files = soup.findAll('a', 'file')
    for file in files:
        # 첨부파일 이름-------------------------------
        file_name = file.text.strip()
        basic_url = 'https://www.sungshin.ac.kr'
        # 첨부파일 주소-------------------------------
        file_url = basic_url + file['href']
        # print(file_name + " " + file_url)

    # 공지사항 본문-----------------------------------
    content = soup.find('div', 'artclView').text.strip()
    # print(content)

    imgs = soup.findAll('img')
    for img in imgs:
        img_src = img['src'][7:]
        # 이미지 주소---------------------------------
        img_url = 'http://' + parse.quote(img_src)
        # print(img_url)

def crawling_bypage(url, page, list):
    url = url + '?page=' + str(page)
    req = requests.get(url)
    # html 소스 가져오기
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    tbody = soup.find('tbody')
    trs = tbody.findAll('tr')

    # 전체 공지사항 갯수 구하기
    total_trs = len(trs)
    # print(total_trs)

    # 고정된 공지사항 갯수 구하기
    headline_trs = soup.findAll('tr', 'headline')
    fixedNum = len(headline_trs)

    # 고정된 공지사항을 제외한 공지
    trs_mn = trs[fixedNum:total_trs]
    for tr in trs_mn:
        # 글번호-------------------------------------
        number = int(tr.find('td', '_artclTdNum').text)
        # print(number)
        basic_url = 'https://www.sungshin.ac.kr'
        # 공지사항 url
        href = basic_url + tr.find('a')['href']
        list.append(href)

def crawling(url, page):
    list = []
    for i in range(1, page + 1):
        crawling_bypage(url, i, list)
    for url in list:
        get_content(url)

# 학사공지
crawling(hacksa, 10)
# 일반공지
crawling(normal, 10)
# 입학공지
crawling(admission, 3)
# 취업공지
crawling(employment, 10)
# 대학원(외국인)공지
crawling(graduated_foreigner, 2)







