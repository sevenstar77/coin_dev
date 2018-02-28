# coinone_dev API SERVER

### 목적
coinone API 를 이용하여 각종 서비스를 제공해주는 API Service(json 기반)

### 역할

 - 등록한 조건에 해당하는 경우 자동 주문 거래
 - 등록한 스케쥴 정보를 이용하여 고객에게 알려주는 기능(email)
 
 - API Server      
    - restframework : alerm스케쥴 등록, order 스케쥴 등록, DB서버 연결,
    - coin one api gateway 기능
    - celery 를 이용한 스케쥴 task 처리
  

### Structure
- scripts/ : 초기 설치 및 실행에 필요한 쉘 스크립트

- gateway : 외부 api등의 Gateway 모듈
	- cointone/ : cointone gateway
		- client : gateway 통신 모듈
			-  `validate_helpers.py` : 유효성 검사 유틸
			-  `cache_manager.py` : 캐시 관리
			-  `mssql_field.py` : MS-SQL용 필드
			-  `redisutil.py` : redis cache 커스텀 설정
			-  `timeutil.py` : 시간 관련
- utils : 각종 유틸리티 모듈
    - mail/ : mail 관련
       - `mail.py` : mail 발송 관련 
- coin_dev : coin_dev프로젝트 
  - `celery.py` : celery 모듈
  - `secret.py` : 비밀키관련 정보
  - `settings.py` : 프로젝트 설정
  - `urls.py` : URL CONF
  - `urls_api.py` : 각 app 접근 api URL CONF
  - `wsgi.py`: wsgi 모듈
- account : 계좌 관련 app
  - `managers.py` : 계좌관련 모델 메니져
  - `models.py` : 계좌관련 모델
  - `serializers.py` : 계좌관련 serializers
  - `test.py` : 계좌관련 Test code
  - `urls.py` : 계좌관련 URL CONF
  - `views.py`: 계좌관련 views 
- order : 주문 관련 app
  - `managers.py` : 주문 모델 메니져
  - `models.py` : 주문 모델
  - `serializers.py` : 주문 serializers
  - `test.py` : 주문 Test code
  - `urls.py` : 주문 URL CONF
  - `views.py`: 주문 views
- schedules : 스케쥴 관련 app
  - `managers.py` : 스케쥴 모델 메니져
  - `models.py` : 스케쥴 모델
  - `serializers.py` : 스케쥴 serializers
  - `test.py` : 스케쥴 Test code
  - `urls.py` : 스케쥴 URL CONF
  - `views.py`: 스케쥴 views
- user : 사용자 관련 app
    -  auth/ : 인증 관련 모듈
        -  `__init__.py `
        -  `base_user_model.py` : customer user class
        -  `password.py` : password
        -  `setting_backed.py` : authenticated module
        -  `token.py` : token module
  - `managers.py` : 사용자 모델 메니져
  - `models.py` : 사용자 모델
  - `serializers.py` : 사용자 serializers
  - `test.py` : 사용자 Test code
  - `urls.py` : 사용자 URL CONF
  - `views.py`: 사용자 views

##API INFO
### sample rq/rs 는 doc/sample/RqRs 경로에 위치해 있습니다.
 - http://127.0.0.1:8000/api/v1.0/schedules/emailschedules : 자동메일 스케쥴 등록 api
 - http://127.0.0.1:8000/api/v1.0/schedules/scheduledetail : 자동메일 스케쥴 변경/삭제 api
 
 - http://127.0.0.1:8000/api/v1.0/schedules/schedule : 자동 메일 스케쥴 api
 
## 
  - 스케쥴 task(celery) : broker 는 redis 를 이용한  처리

###TO-DO LIST 
  - test code 작성 : TDD로 개발 하고 싶었으나 다른 사정등으로 인하여 못함, 자동화 및 안정성을 위하여 작성할것
  - DB 관련 : 다른 SQL 교체, 관계형 테이블에 맞게 새롭게 테이블 생성할것 (index, Foreinkey settings 등) 
  - script 관련 자동 script 관련 명렁어 만들것
  - permission 관련 : 현재  permission 의 경우 전부 allowAny 로 접근 변경할것 
  - 평균단가 api 확인하여 로 수익률 퍼센트 계산 후 자동 로직 완성시킬것
  
##Development enviroment
 - OS : windows 10, Docker Image : ubuntu 16.04)
 - IDE : Pycharm
 - DB : sqlite3
 - Python(3.5.4), Django(1.11.9),Djangorestframework(3,7,5) celery, redis, requests,simplejson, 
 - coinone API V2

# E-MAIL
 * amazonprimeday777@gmail.com