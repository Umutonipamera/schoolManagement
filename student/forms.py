
 
from django import forms


from django import forms
from django.forms import fields
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
          model= Student
          fields= "__all__"