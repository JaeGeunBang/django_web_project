## DJango



### 가상환경 셋팅 

PyCharm IDE를 설치후 가상환경을 만들것

- File > Setting > Project: 프로젝트 폴더명 > Python Interpreter



셋팅후 아래와같이 가상환경을 실행할 수 있다.

```
venv/Scripts/activate.bat
```



가상환경 내에서 django를 설치한다.

```
pip install django
```



장고 프로젝트를 생성한다.

```
django-admin startproject backend .
```

- 생성후 `backend/`, `manage.py` 가 생성됨을 확인한다.



Django 서버를 실행한다.

```
python manage.py runserver
```

- 실행후 `http://127.0.0.1:8000` 에 접속해볼수있다.



### 프로젝트 설명

- 프로젝트 폴더내 들어가보면, 다양한 .py 파일들이 있음.
- urls.py
  - 사용자가 어떤 URL 형식으로 접근했을 때, 어떻게 웹사이트를 작동시킬지에 대해 정리해둠
  - `localhost:8000/admin` 에 접속시 admin site 로 안내해줌

```
urlpatterns = [
	path('admin/', admin.site.urls)
]
```



- settings.py
  - 장고 프로젝트의 설정을 담고있음



### 데이터베이스 생성

```
python manage.py migrate
```

- 위 명령을 수행후 db.sqlite3 이 생성됨을 볼수 있다.
  - SQLite3은 특정 파일 하나로 데이터베이스를 관리할 수 있다.
  - 실제 운영 환경에서는 MySQL, MongDB를 사용해야함

### 관리자 생성

```
python manage.py createsuperuser
```

- 웹페이지의 관리자를 생성후, `http://localhost:8000/admin` 에 접속해보면 관리자 로그인 화면이 뜬다.



### 앱 생성 방법

- 장고는 1개 이상의 앱으로 구성되며, 앱은 특정한 기능을 수행하는 단위 모듈이다.
- 예를들어, 블로그, 갤러리, 방명록 3가지를 개발하고 싶다면, 3개의 앱을 만들면 된다.

```
python manage.py startapp blog
python manage.py startapp pages
```





### 모델을 DB에 생성하는 방법

- 생성한 App에 `models.py` 아래와 같은 model을 위한 class를 추가한다.

```
from django.db import models

class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField
```

- 이후 settings.py에  `INSTALLED_APPS`에 생성한 App 이름을 기재한 이후 아래 명령을 수행한다.
  - 수행후 migration/0001_initial.py 파일이 생성된것을 볼수있다.
  - 최초 makemigrations 실행시 생성되는 파일이다.

```
python manage.py makemigrations

..
 - Create model Post
```



- 실제 데이터베이스에 위에서 생성한 Post 모델을 적용하기 위해 아래 명령을 수행한다.

```
python manage.py migrate
```



- 위에서 생성한 Post 모델은 admin 페이지에서 쉽게 파악할 수 있다.
  - admin.py에 아래 구문을 추가한다.
  - 이후 admin 페이지에 접속하면 Post 모델을 추가할 수 있다.

```
from .models import Post

admin.site.register(Post)
```



### 모델 수정

- 위에서 생성한 `model.py` 에 신규 컬럼을 추가한다고 가정하자.

```
...
updated_at = models.DateTimeField(auto_now=True)
...
```

- 이후 makemigrations을 통해 장고에게 알려주고, migrate를 통해 데이터베이스에 반영한다. 이후 서버를 재실행 해야한다.

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
