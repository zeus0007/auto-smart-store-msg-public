# 스마트스토어 주문 카톡으로 받기 & 하루에 여러번 받기
하루에 스마트스토어 주문 현황이 기존 네이버 메일 1번에서 더 '짧은 주기로','카톡으로' 받고 싶어서 제작 😊</br>
</br>
카톡에서 나에게 보내기 기능 이용.</br>
</br>
Tip. 나에게 보내기를 상단에 고정하면 실시간 주문 현황 확인 가능.
</br>
</br>

## How to use?
### 1. 파이썬 설치
### 2. git clone
### 3. config.py 만들고 아래 내용 작성해서 입력
KAKAO_TOKEN = '카카오 개발자 토큰(나에게 보내기 설정 후)'
NAVER_ID = '본인 네이버 아이디'
NAVER_PASSWORD = '본인 네이버 비밀번호'
### 4. 아래 명령어 command 창에 입력
pip install selenium ChromeDriverManager BeautifulSoup time schedule json requests
### 5. python3 smartstore.py
</br>
</br></br></br></br>

Last updated on 2021.02.05