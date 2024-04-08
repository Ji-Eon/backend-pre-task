# Dockerfile
FROM python:3.9.3

## 환경변수 셋팅
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ=Asia/Seoul

# Debian/Ubuntu 기반 이미지의 경우
RUN apt-get update && apt-get install -y graphviz libgraphviz-dev pkg-config

## slim-buster에 필요한 라이브러리 설치
RUN apt-get update && apt-get -y install  --no-install-recommends libpq-dev libgtk2.0-dev libgl1-mesa-glx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 폴더 생성
RUN mkdir -p /usr/src/app

# 작업 폴더 설정
WORKDIR /usr/src/app

# 폴더 복사
COPY . .

# pip 업그레이드
RUN pip3 install --upgrade pip
#RUN pip3 install django

# 캐시를 사용하지 않아서 설치는 오래걸리지만 항상 해당 시점에 맞는 패키지 설치 가능
#RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
