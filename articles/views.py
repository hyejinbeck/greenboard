from django.shortcuts import render, redirect
from .models import Article
# models.py 의 Article 을 불러오겠다. 
# Article 에는 제목,내용,작성시간이 있으니 
# 불러와서 아래의 구성으로 보여주게 한다. 
from .forms import ContactForm
# forms.py의 ContactForm을 불러오겠다. 

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
    if request.method == 'POST': # post요청일때 
        contact_eng = ContactForm(request.POST)   # 프론트엔드에 검증
        if contact_eng.is_valid():           #통과되면 백엔드에 재검증
            contact_eng.save()            # 다 통과된것만 저장 

            return redirect('articles:index') # 일단 index로 보내보자.     
        
    else: 
        contact_eng = ContactForm()

    context = {
        'contact_eng': contact_eng,
    }

    return render(request, 'contact.html', context)

def resume(request): 
    pass

def projects(request): 
    pass

def daily(request): 
    pass