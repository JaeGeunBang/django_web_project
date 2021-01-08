from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.single_post_page), # 정수 형태의 값을 pk 하는 변수로 담는다는 의미
    path('', views.index) # blog/ 가장 기본 url
]