from django import forms
from .models import *

class Insert_subject(forms.ModelForm):
    class Meta: 
        model = Subject
        fields = '__all__'
        
class Insert_major(forms.ModelForm):
    class Meta:
        model = Major
        fields = '__all__'
        
class Delete_major(forms.ModelForm):
    class Meta:
        model = Major
        fields = '__all__'
        
class Edit_major(forms.ModelForm):
    class Meta:
        model = Major
        fields = '__all__'


        
class Insert_student(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
class Delete_student(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
class Edit_student(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'