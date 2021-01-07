## DJango



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