from django import forms
from .models import Posts, GuestbookEntry

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'


class GuestbookEntryForm(forms.ModelForm):
    class Meta:
        model = GuestbookEntry
        fields = ['name','message']
        widgets = {
            'message' : forms.Textarea(attrs={'rows':5}),
        }