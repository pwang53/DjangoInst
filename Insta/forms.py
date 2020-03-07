from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from Insta.models import InstaUser

# forms defined here handles user inputs

class CustomUserCreationForm(UserCreationForm):
    # Meta是元数据
    class Meta(UserCreationForm.Meta):
        # 所对应的model是自己创建的customized model
        # 并且要告知有哪些field
        model = InstaUser
        fields = ('username', 'email', 'profile_pic')