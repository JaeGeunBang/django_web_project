## Django



### 목차

- 가상환경 셋팅
- 프로젝트 파일 설명
- 데이터베이스 생성 (SQLite3)
- 앱 생성
- 모델을 DB에 생성 및 수정
- 웹 페이지 생성 후 URL 설정
- 테스트 코드 작성

- 장고 쉘 



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

```python
from django.db import models

class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField
```

- 이후 settings.py에  `INSTALLED_APPS`에 생성한 App 이름을 기재한 이후 아래 명령을 수행한다.
  - 수행후 migration/0001_initial.py 파일이 생성된것을 볼수있다.
  - 최초 makemigrations 실행시 생성되는 파일이다.

```python
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

```python
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



### 웹 페이지 생성 후 URL 설정하기

- url은 urls.py에서 내용을 추가해야한다.
  - 아래와 같이 추가하면, /blog url 접속시 blog.urls를 포함한다는 의미이다.
  - 이는, blog 폴더 내 `urls.py`에 관련 내용을 추가해주어야 한다.

```python
urlpatterns = [
    path('blog/', include('blog.urls')),
	...
]
```

- blog내 urls.py에서 내용을 추가한다.
  - 특정 추가 path없이 /blog 로 들어올 경우, views.index를 실행한다.
  - views.py를 생성한다.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
]
```

- blog내 views.py를 생성 후 아래 내용을 추가한다.
  - blog내 index.html를 반환해주기 위해, blog 내 templates/blog/index.html를 생성 후 재시도를 해본다.

```python
from django.shortcuts import render

# Create your views here.

def index(request) :
    return render(
        request,
        'blog/post_list.html',
    )
```



### 테스트 코드 작성

- 테스트 주도 개발 (TDD) 란?
  - 바로 개발부터 하는것이 아닌, 개발하려는 항목에 대한 점검 사항을 테스트 코드로 만들면서 진행하는 방식
  - 단계
    - 1. 테스트 코드 작성
         - 만들고 싶은 기능을 점검할 코드 작성
         - 기능 구현을 하지 않았기 때문에 테스트 결과는 실패할것.
      2. 기능 구현
         - 테스트 코드를 만족시킬수 있게 기능 구현
         - `테스트 통화를 최우선으로 생각하고 작업`함
      3. 리팩토링
         - 기능의 성능을 향상, 재상용성을 좋게하거나, 가독성이 좋은 코드로 개선
         - 테스트 코드로 다시 점검

- 테스트 코드는 tests.py에 아래와 같이 작성할수 있다.

```python
from django.test import TestCase

# Create your tests here.
class TestView(TestCase):
    def test_post_list(self):
        self.assertEqual(2, 2)
```

- 이후 python manage.py test를 하여, 테스트 코드를 수행할 수 있다.



### 장고 쉘

- 장고 쉘을 통해 지금까지 개발한 내용을 테스트해볼수 있다.
- 아래 명령을 통해 실행한다.

```
> python manage.py shell
```

- 앞서 생성한 Post, Category 정보를 조회해본다

```
> from blog.models import Post, Category
> Post.objects.count()
6
> Category.objects.count()
3
> exit()
```

- 장고쉘 뿐만 아니라 `장고 쉘 플러스`를 통해 더 확장된 기능을 사용할 수 있다. 
- 설치

```
> pip install django_extensions
> pip install ipython
```

- seetings.py에 아래 내용 추가

```
INSTALLED_APPS = [

 ...
 'django_extensions',
]
```

- 실행

```
> python manage.py shell_plus
```

