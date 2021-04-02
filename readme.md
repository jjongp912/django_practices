#django Practice

## 장고 프로젝트(django_practices) 만들기

### 1. pycharm에서 프로젝트 생성

### 2. django library 설피 (터미널)
```shell
(nenv)# pip install django
```
### 3. mysqlclient library 설치
```shell
(env) # pip install mysqlclient
```

### 4. 장고 프로젝트 생성
```shell
(env) # django-admin startproject django_practices
```
### 5. 디렉토리 정리(pycharm 프로젝트랑 장고 프로젝트를 일치시켜 주기)

### 6. 초기 설정 (s)
1) time zone 설정
```python
TIME_ZONE = 'Asia/Seoul'
```


2) databese 설정
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webdb',
        'USER': 'webdb',
        'PASSWORD': 'webdb',
        'HOST': 'localhost',
        'PORT':3306
    }
}
```
### 7. 장고 프로젝트의 관리 어플리케이션(기본설치)이 자용하는 DB 생성하기
```shell
(env) # python manage.py migrate
```
* mysql5.1 인 경우 오류가 발생하면, manage.py에 다음 코드를 추가하고 다시 실행
```python
from django.db.backends.mysql.base import DatabaseWrapper
DatabaseWrapper.data_types['DateTimeField'] = 'datetime'
```

### 8. 프로젝트(사이트) 관리 계정 만들기
```shwll
(env) # python manage.py createsuperuser
```
### 9. 지금까지 작업 내용 확인
1) 서버 시작하기
```shell
(env) # python manage.py runserver 0.0.0.0:9999
```   

2) 브라우저로 접근하기
url http://localhost:9999 로 접근

-----------------------------------------------------------------
## 2. 프로젝트(django_practices)에 만들기

### 1. Application등의 통합 template 디렉토리 templates 만들기
1) 디렉토리 생성
django_practices
|--- templates

2) template 디렉토리 설정(settings.py)
```python
import os
.
.
.
'DIRS': [os.path.join(BASE_DIR, 'templates')]

```

### 2. helloworld application 만들기
!) application 생성
```shell
(venv) # python manage.py startapp helloworld
```
2) application 등록(settings.py)
```python
INSTALLED_APPS = [
    'helloworld',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
3) application의 template 디렉토리 생성
django_practices
|--- templates
        |--- helloworld
   
4) urls.py 에 URL 등록하고 viwes.py에 요청 처리 함수를 만들고 template(html) 연결하고...(반복반복)









