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

# 컴퓨터공학과
print('컴퓨터공학과===========================================================')
crawling(computer, 10)
crawling(computer_hire, 3)

# 청정융합에너지공학과
print('청정융합에너지공학과===========================================================')
crawling(cleanEnergy_hire, 1)
crawling(cleanEnergy_outdoor, 1)

# 바이오생명공학과
print('바이오생명공학과===========================================================')
crawling(biotechnology, 7)
crawling(biotechnology_hire, 1)

# 바이오식품공학과
print('바이오식품공학과===========================================================')
crawling(biofood_notice, 6)

# 융합보안공학과
print('융합보안공학과===========================================================')
crawling(security, 7)
crawling(security_hire, 2)

# 정보시스템공학과
print('정보시스템공학과===========================================================')
crawling(informationSystems, 7)

# 서비스디자인공학과
print('서비스디자인공학과===========================================================')
crawling(serviceDesign, 6)
crawling(serviceDesign_hire, 1)
crawling(serviceDesign_outoor, 1)

# AI융합학부
print('AI융합학부===========================================================')
crawling(ai, 1)
crawling(ai_outdoor, 1)

# 국어국문학과
print('국어국문학과===========================================================')
crawling(korean, 10)
crawling(korean_outdoor, 5)
crawling(korean_hire, 5)

# 영어영문학과
print('영어영문학과===========================================================')
crawling(english, 10)
crawling(english_outdoor, 1)
crawling(english_hire, 5)

# 독일어문/문화학과
print('독일어문/문화학과===========================================================')
crawling(german_outdoor, 1)
crawling(german_hire, 5)

# 프랑프어문/문화학과
print('프랑프어문/문화학과===========================================================')
crawling(french, 1)
crawling(french_outdoor, 1)
crawling(french_hire, 3)

# 일본어문/문화학과
print('일본어문/문화학과===========================================================')
crawling(japanese_hire, 5)

# 중국어문/문화학과
print('중국어문/문화학과===========================================================')
crawling(chinese_outdoor, 1)
crawling(chinese_hire, 3)

# 사학과
print('사학과===========================================================')
crawling(history_outdoor, 1)
crawling(history_hire, 5)

# 교육학과
print('교육학과===========================================================')
crawling(education_hire, 5)

# 사회교육과
print('사회교육과===========================================================')
crawling(socialEdu_hire, 5)

# 윤리교육과
print('윤리교육과===========================================================')
crawling(EthicsEdu_hire, 5)

# 한문교육과
print('한문교육과===========================================================')
crawling(chineseEdu_hire, 5)

# 유아교육과
print('유아교육과===========================================================')
crawling(childhoodEdu_hire, 5)

# 수학과
print('수학과===========================================================')
crawling(math_hire, 2)

# 통계학과
print('통계학과===========================================================')
crawling(statistics_hire, 2)

# it학부
print('it학부===========================================================')
crawling(it_hire, 3)

# 수리통계데이터사이언스학부
print('수리통계데이터사이언스학부===========================================================')
crawling(dataScience_outdoor, 1)

# 뷰티산업학과
print('뷰티산업학과===========================================================')
crawling(beauty, 3)
crawling(beauty_hire, 1)

# 문화예술경영학과
print('문화예술경영학과===========================================================')
crawling(cultureArt, 2)

# 현대실용음악학과
print('현대실용음악학과===========================================================')
crawling(music, 5)

# 무용예술학과
print('무용예술학과===========================================================')
crawling(danceArt, 3)

# 스포츠레저학과
print('스포츠레저학과===========================================================')
crawling(danceArt, 5)





