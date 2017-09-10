from django import forms
from .models import Opinion,Question

class leaveOpinionForm(forms.Form):
    name=forms.CharField(label='ФИО', max_length=40)
    email=forms.EmailField()
    opinion=forms.CharField(label='Отзыв',max_length=150)
    image = forms.ImageField(label='Картинка')
    class Meta:
        model=Opinion
        fields=['name','email','opinion','image']
        widgets={
            'opinion':forms.Textarea(attrs={'row':5})
        }

class AskForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=['name','email','telephone','question']
