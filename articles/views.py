from django.shortcuts import render
from .models import Article
# models.py 의 Article 을 불러오겠다. 
# Article 에는 제목,내용,작성시간이 있으니 
# 불러와서 아래의 구성으로 보여주게 한다. 

# Create your views here.
def index(request): 
    articles = Article.objects.all().order_by('-id') #최신글먼저로 역순정렬 order_by('-id') 
    # 가져오는 Aarticle의 모든것을 articles변수화 

    context = {        # 보여지는 내용은 
        'articles' : articles ,   # articles변수 
    }

    return render(request, 'index.html', context)
            # 요청값은, index.html로 보여지며, 안에 내용이 들어있다.

def contact(request): 
    pass 

def resume(request): 
    pass

def projects(request): 
    pass

def daily(request): 
    pass