from django.urls import path 
from . import views  
# views.py 가져오기 

app_name = 'articles'   # app 이름

urlpatterns = [
    path('',views.index, name='index'),
    # 기본 articles/   => index라고 부르겠다. 
    # 기본 index.html 페이지는 views.py의 detail함수를 사용해서 보여진다. 
    path('contact/', views.contact, name='contact'), # 추가 
]