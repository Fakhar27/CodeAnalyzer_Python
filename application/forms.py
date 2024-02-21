from django import forms
from application.models import Uploadfile


class fileForm(forms.ModelForm):
    class Meta:
        model = Uploadfile
        fields = {'file'}