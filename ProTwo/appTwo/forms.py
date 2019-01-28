from django import forms
from appTwo.models import User

class NewUserForm(forms.ModelForm):
    # incase you want to add own custom validator etc
    class Meta():
        model = User
        fields = '__all__'
