
<h1 align="center">Welcome to KidsNote_backend-pre-task 👋</h1>


### DOCKER 실행방법
- ./dev_script.sh 실행 또는 docker-compose -f docker-compose.yaml up --build 에서 Docker를 실행해 줍니다.
- 현재 requirements.txt 및 확인자 분의 환경에 영향을 미치지 않게 하기 위해 Docker로 구성하였습니다.
- Docker를 실행하고 나면 localhot:8000/admin/을 통해 Django Admin에 접속할 수 있습니다.

<p align="center">
  <img src="https://github.com/Ji-Eon/KidsNote_backend-pre-task/blob/main/KIDS_TOOLS/git_images/docker_running.png?raw=true">
</p>


### DOCKER 환경 기반 Django Admin Superuser 생성하기
- docker ps 명령어를 통해 Container id를 확인합니다.
- docker exec -it {Container_id} /bin/bash 로 Docker Container로 진입합니다.
- python manage.py createsuperuser를 입력하여 Django SuperUser 계정을 생성합니다.


### Python Module

- python : 3.9.3
- django : 3.2.20
- django-rest-framework : 3.14.0
- drf-yasg : 1.21.7

### Database
- SQLite

### Swagger 및 연락처 관리 API

이 문서는 로컬 환경에서 연락처 관리 API를 사용하기 위한 가이드를 제공합니다.

## 시작하기

API 문서에 접근하려면 브라우저를 통해 [localhost:8000/swagger/](http://localhost:8000/swagger/)에 접속하세요.

<p align="center">
  <img src="https://github.com/Ji-Eon/KidsNote_backend-pre-task/blob/main/KIDS_TOOLS/git_images/swagger_ui.png?raw=true">
</p>

## API 엔드포인트

- `POST /contact/data`: 데이터셋을 미리 정의하였으며, 해당 API 호출 시 ERD에 정의된 대로 데이터가 데이터베이스에 저장됩니다.
- `GET /contact/list`: 저장된 연락처 목록을 조회합니다.
- `GET /contact/sort`: 연락처 목록을 조회하고 필요에 따라 이름(name), 이메일(email), 전화번호(phone_number)로 정렬합니다. 정렬 순서는 쿼리 파라미터를 통해 지정할 수 있습니다.
- `GET /contact/search`: id 값을 통해 특정 연락처의 정보를 디테일하게 조회할 수 있습니다.
- `POST /contact/create`: 새로운 연락처를 생성할 수 있습니다.

## 기술 스택

- Django REST Framework: 연락처 데이터를 관리하고 RESTful API를 제공합니다.
- drf-yasg: Swagger를 통한 API 문서 자동화를 지원합니다. 

## 사용 방법

각 API의 상세한 사용 방법은 Swagger 문서를 참고하시기 바랍니다. 예를 들어, `/contact/sort` 엔드포인트는 다음과 같이 사용할 수 있습니다:


## data Upload DjangoAdmin 입력 결과 화면
- `POST /contact/data` : API를 호출하면 이미지와 같이 데이터가 자동으로 저장 됩니다.

<p align="center">
  <img src="https://github.com/Ji-Eon/KidsNote_backend-pre-task/blob/main/KIDS_TOOLS/git_images/data_contents_result.png?raw=true">
</p>


## Contact ERD Description

-  `Contact` 연락처 세부 정보를 담고 있는 모델, 

-  `CompanyInfo` 회사 이름과 직책을 포함한 정보를 담고 있는 모델

-  `Label` 모델은 연락처를 분류하는 데 사용되며, 각 연락처에 하나 이상의 라벨을 연결할 수 있습니다.

<p align="center">
  <img src="https://github.com/Ji-Eon/KidsNote_backend-pre-task/blob/main/KIDS_TOOLS/db/contact_erd.png?raw=true">
</p>

## Developer

👤 **Ji-Eon**
=======

* Github: [@Ji-Eon](https://github.com/Ji-Eon)

## Show your support

Give a ⭐️ if this project helped you!
