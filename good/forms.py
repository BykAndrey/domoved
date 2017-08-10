from django import forms
from .models import Opinion,Question

class leaveOpinionForm(forms.ModelForm):
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