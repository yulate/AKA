from django.forms import ModelForm
from .models import Api_message, Api_user

class Api_messageFrom(ModelForm):
    class Meta:
        model = Api_message
        fields = ['text']
        labels = {'text': ''}
class Api_userForm(ModelForm):
    class Meta:
        model = Api_user
        fields = ['username', 'password', 'vip', 'score']