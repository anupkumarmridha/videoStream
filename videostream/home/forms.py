from django import forms
from home.models import Video,Category

choices=Category.objects.all().values_list('name','name')
choices_list=[]
for cats_item in choices:
    choices_list.append(cats_item)

class PostVideoForm(forms.ModelForm):
    class Meta:
        model=Video
        fields=('title', 'video','category', 'author')
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the Title'}),
            'category': forms.Select(choices=choices_list ,attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'', 'id':'user_id', 'type':'hidden'}),
            }

class EditVideoForm(forms.ModelForm):
    class Meta:
        model=Video
        fields=('title', 'video','category', 'author')
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the Title'}),
            'category': forms.Select(choices=choices_list ,attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'', 'id':'user_id', 'type':'hidden'}),
            }