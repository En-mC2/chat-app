from django.forms import ModelForm
from .models import Room
#from django.contrib.auth.models import User
from .models import User
from django.contrib.auth.forms import UserCreationForm

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host','participants']
    

class UserForm(ModelForm):
    class Meta:
        model = User
        fields=['name','username','email','avatar','bio']

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','email','password1','password2']