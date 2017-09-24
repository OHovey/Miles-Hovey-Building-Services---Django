from django import forms
from .models import Project, Image


class ProjectForm(forms.ModelForm):
    class Meta:

        model = Project
        fields = ('overview', 'description_of_work')

class ImageForm(forms.ModelForm):
    class Meta:

        model = Image
        fields = ('picture',)
        
