from django.urls import path
from . import views

urlpatterns = [
    #path('<int:pk>/', views.single_post_page), # 정수 형태의 값을 pk 하는 변수로 담는다는 의미 (FBV 방식)
    #path('', views.index) # blog/ 가장 기본 url (FBV 방식)
    path('<int:pk>/', views.PostDetail.as_view()), # 정수 형태의 값을 pk 하는 변수로 담는다는 의미 (CBV 방식)
    path('', views.PostList.as_view()) , # blog/ 가장 기본 url (CBV 방식)
]