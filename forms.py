from django import forms


class UploadFileForm(forms.Form):
    images = forms.ImageField()
    group = forms.CharField()

