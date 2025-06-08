from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Posts, Statements, Document, GuestbookEntry
# Register your models here.
class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(config_name='default'))

    class Meta:
        model = Posts
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Posts, PostAdmin)
#admin.site.register(Posts)
admin.site.register(Statements)
admin.site.register(GuestbookEntry)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title','doc_type', 'uploaded_time')
    list_filter = ('doc_type',)
    ordering = ('-uploaded_time',)