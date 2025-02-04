from django import forms
from django.forms import ModelForm
from .models import Bid,VideoBase


class BidForm(ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Введите имя')
    # surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Введите Фамилия')
    # phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
    #                                label='Введите номер телефона')
    # messages = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
    #                            label='Введите комментарий')
    class Meta:
        model = Bid
        fields = ('name', 'surname', 'phone_number', 'messages')

class CustomFileFirm(ModelForm):
    cleaned_data = forms.BooleanField(required=False, label='Удалить файл')

    class Meta:
        model = VideoBase
        fields = '__all__'

    def sava(self,commit=True):
        instance=super().save(commit=False)
        if self.cleaned_data.get('clear_file') and instance.video_file:
            instance.video_file.delete(sava=False)
            instance.video_file = None
        if commit:
            instance.save()
        return instance