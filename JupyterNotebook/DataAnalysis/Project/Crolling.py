

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip
import time
import csv

# chromedriver 설정
driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)

# 네이버 로그인 페이지로 이동
driver.get('https://nid.naver.com/nidlogin.login')

# id와 password 정보 가져오기
idwd = "{}"
pswd = "{}"


# id와 password 입력
pyperclip.copy(idwd)
driver.find_element(By.ID,"id").send_keys(Keys.CONTROL,'v')
time.sleep(0.5)
pyperclip.copy(pswd)
driver.find_element(By.ID,"pw").send_keys(Keys.CONTROL,'v')
time.sleep(0.5)

# 로그인 버튼 클릭
driver.find_element(By.ID,"log.login").click()
# 자주 사용하는 브라우저 등록 해제
driver.find_element(By.ID,'new.dontsave').click()

# 네이버 메일로 이동
#원하는 메일 끝번호 입력
mail_num = 33659
buff =[]
#아래부터 100개 메일 가져옴
for i in range((mail_num-300),mail_num):
    print(i)   
    
    driver.get(f'https://mail.naver.com/v2/read/0/{i}')


    #title = driver.find_element(By.XPATH, '//*[@id="mail_read_scroll_view"]/div/div[1]/h4/span[2]/span/span[2]')
    #print(title.text)
    contents_table = driver.find_element(By.XPATH, '//*[@id="mail_read_scroll_view"]/div/div[2]')
    # 테이블 내 모든 텍스트 추출
    buff.append(contents_table.text)
    time.sleep(0.5)
    
#임시로 csv파일 하나 만들고 주소 입력해주세요
with open('JupyterNotebook\DataAnalysis\Project\crollingdata.csv', 'w+', newline='',encoding='utf-8') as csvfile:
    
    writer = csv.writer(csvfile)
    for row in buff:
        writer.writerow(["ham",row,])



    