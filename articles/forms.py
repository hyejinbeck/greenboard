from django import forms 
from .models import Article 
# models.py에서 Article 클래스를 불러온다. 
# Article클래스는 제목,내용,작성시간 으로 구성되있다. 

class ContactForm(forms.ModelForm): 
    
    class Meta: 
        model = Article       # Article 의 
        fields = '__all__'     # 모든 구성내용을 보여줘(제목,내용,작성시간)