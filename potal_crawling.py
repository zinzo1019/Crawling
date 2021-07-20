from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver

# 드라이버 가져오기
driver = webdriver.Chrome('C:\chromedriver\chromedriver_win32\chromedriver.exe')
# 성신 로그인 페이지에 접속
driver.get('https://portal.sungshin.ac.kr/sso/login.jsp')

sleep(0.5)
# 포탈 아이디
driver.find_element_by_name('loginId_mobile').send_keys('너의 학번')
sleep(0.5)
# 포탈 비밀번호
driver.find_element_by_name('loginPwd_mobile').send_keys('너의 비밀번호')
# 로그인 버튼 누르기
driver.find_element_by_xpath('//*[@id="login_mobile"]/div[1]/div/ul/li/ul/div/fieldset/a').click()

# 열심히 했는데 해도 그만 안 해도 그만이라서 주석 처리함. 지금 매우 슬픔.
# sleep(0.5)
# # 비밀번호 변경하라는 창 지우기
# driver.find_element_by_class_name("pop_close").click()
# # 메뉴바를 포함한 태그와 아이디 연결
# menu_bar = driver.find_element_by_id('gnbMobile')
# # 메뉴바 클릭
# menu_bar.find_element_by_class_name('btn_menu').click()
#
# # 포탈공지 클릭
# header_div = driver.find_element_by_id('header')
# depth_1_li = header_div.find_elements_by_tag_name('li')
# depth_1_li[42].click()
# depth_2_li = depth_1_li[42].find_elements_by_tag_name('li')
# depth_2_a = depth_2_li[0].find_element_by_tag_name('a')
# depth_2_a.click()

def crawling_bypage(page):
    print("학부학사 " + str(page) + "페이지------------------------------------------------------------------------------")
    if page >= 12:
        page = page % 10
    if page >= 22:
        page = page % 10
    if page >= 32:
        page = page % 10
    pageIndex = driver.find_element_by_id('pageIndex')
    nexts = pageIndex.find_elements_by_tag_name('a')
    # 페이지 이동
    nexts[page + 1].click()
    url = driver.page_source
    soup = BeautifulSoup(url, "html.parser")
    titles = soup.findAll('span', {"id": "inTtl"})
    for title in titles:
        print(title.text.strip())


# 포탈공지에서 제목 크롤링
def potal_notice():
    driver.get('https://portal.sungshin.ac.kr/portal/ssu/menu/notice/ssuboard01.page')

    # iframe에 접근하기 위해 변환
    driver.switch_to.frame('IframePortlet_8654')
    url = driver.page_source
    soup = BeautifulSoup(url, "html.parser")

    print("포탈공지-----------------------------------------------------------------------------------------------------")
    # 아이디 속성을 지우면 제목과 운영진, 조회수까지 볼 수 있음 -> 얘는 테이블에 저장할 것인가 말 것인가
    titles = soup.findAll('span', {"id": "inTtl"})
    for title in titles:
        print(title.text.strip())

def hacksa():
    driver.get('https://portal.sungshin.ac.kr/portal/ssu/menu/notice/ssuboard02.page')
    driver.switch_to.frame('IframePortlet_8656')
    url = driver.page_source
    soup = BeautifulSoup(url, "html.parser")
    # print(soup)

    print("학부학사 1페이지----------------------------------------------------------------------------------------------")
    # 아이디 속성을 지우면 제목과 운영진, 조회수까지 볼 수 있음 -> 얘는 테이블에 저장할 것인가 말 것인가
    titles = soup.findAll('span', {"id": "inTtl"})
    for title in titles:
        print(title.text.strip())

    # # 테스트 용 (3페이지까지 크롤링)
    # for i in range(2, 4):
    #     crawling_bypage(i)

    # 40페이지까지 크롤링 (최근 1년까지 크롤링)
    for i in range(1, 41):
        crawling_bypage(i)

def scholarship():
    driver.get('https://portal.sungshin.ac.kr/portal/ssu/menu/notice/ssuboard10.page')
    driver.switch_to.frame('IframePortlet_9616')
    url = driver.page_source
    soup = BeautifulSoup(url, "html.parser")
    # print(soup)

    print("학부장학-----------------------------------------------------------------------------------------------------")
    # 아이디 속성을 지우면 제목과 운영진, 조회수까지 볼 수 있음 -> 얘는 테이블에 저장할 것인가 말 것인가
    titles = soup.findAll('span', {"id": "inTtl"})
    for title in titles:
        print(title.text.strip())

    # 17페이지까지 크롤링 (최근 1년까지 크롤링)
    for i in range(1, 18):
        crawling_bypage(i)

    # #테스트 용 (3페이지까지 크롤링)
    # for i in range(2, 4):
    #     crawling_bypage(i)


def rule():
    driver.get('https://portal.sungshin.ac.kr/portal/ssu/menu/notice/schRegulation.page')
    driver.switch_to.frame('IframePortlet_9676')
    url = driver.page_source
    soup = BeautifulSoup(url, "html.parser")
    # print(soup)

    print("학칙개정공고 및 공포-------------------------------------------------------------------------------------------")
    # 아이디 속성을 지우면 제목과 운영진, 조회수까지 볼 수 있음 -> 얘는 테이블에 저장할 것인가 말 것인가
    titles = soup.findAll('span', {"id": "inTtl"})
    for title in titles:
        print(title.text.strip())

potal_notice()
hacksa()
scholarship()
rule()

# 포탈에서 나가기
driver.quit()