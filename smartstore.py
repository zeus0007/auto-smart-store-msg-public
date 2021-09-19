from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import schedule

#로딩 대기
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException


# 카카오 메세지
import os
import json
import requests
import config


login = {
    "id" : config.NAVER_ID,
    "pw" : config.NAVER_PASSWORD,
}

def sendToMeMessage(text):
    KAKAO_TOKEN = config.KAKAO_TOKEN
    header = {"Authorization": 'Bearer ' + KAKAO_TOKEN}

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send" #나에게 보내기

    post = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://sell.smartstore.naver.com/#/home/dashboard/",
            "mobile_web_url": "https://sell.smartstore.naver.com/#/home/dashboard/",
        },
        "button_title": "바로 확인",
    }
    data = {"template_object": json.dumps(post)}
    return requests.post(url, headers=header, data=data)


#네이버 상품 확인
def store_check():
    url = "https://sell.smartstore.naver.com/#/home/about"

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get(url)

    try :
        WebDriverWait(driver, 10).until(
            expected_conditions.invisibility_of_element(
                (By.CSS_SELECTOR, "__initial_loading")
            )
        )
        #스마트스토어 첫페이지
        driver.find_element_by_xpath('/html/body/ui-view[1]/div[2]/div[2]/div/div[1]/div[2]/a[2]').click()
        print("로딩화면 가져오기 성공")
        driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div/div/form/div[1]/ul/li[2]/a').click()
        print("네이버 로그인 화면 전환")
        #네이버 로그인
        time.sleep(0.5) 
        driver.find_element_by_name('id').send_keys(login.get("id"))
        time.sleep(0.5)
        driver.find_element_by_name('pw').send_keys(login.get("pw")) 
        driver.find_element_by_xpath('//*[@id="log.login"]').click()
        print("로그인 완료")
        driver.find_element_by_xpath('//*[@id="new.save"]').click()
        print("기기등록 완료")
        WebDriverWait(driver, 10).until(
            expected_conditions.invisibility_of_element(
                (By.CSS_SELECTOR, "__initial_loading")
            )
        )
        bsObject = BeautifulSoup(driver.page_source, "html.parser")
        content = bsObject.select('#seller-content > ui-view > div > div.seller-sub-content > div > div.panel-wrap.flex-col-6.flex-col-xs-12.order-md-1.order-xs-1 > div > div.panel-body.flex.flex-wrap > div.list-wrap.deposit-list.flex-col-6.flex-col-md-12 > div > ul > li:nth-child(2) > span.number-area > a')
        print(content[0].text)
        new_order = content[0].text
        content = bsObject.select('#seller-content > ui-view > div > div.seller-sub-content > div > div.panel-wrap.flex-col-6.flex-col-xs-12.order-md-1.order-xs-1 > div > div.panel-body.flex.flex-wrap > div.list-wrap.delivery-list.flex-col-6.flex-col-md-12 > div > ul > li:nth-child(1) > span.number-area > a')
        print(content[0].text)
        ready_order = content[0].text
        # 카톡으로 결과 전송
        text = f"현재 신규 주문 건수 {new_order}\n현재 배송 대기 건수 {ready_order}"
        print(sendToMeMessage(text).text)
        
    except ElementNotVisibleException:
        print("로딩화면 대기 실패")

schedule.every().hours.do(store_check)
while True:
    schedule.run_pending()
    time.sleep(1)


