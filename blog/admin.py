from django.contrib import admin
from .models import Posts, Statements, Document
# Register your models here.


admin.site.register(Posts)
admin.site.register(Statements)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title','doc_type', 'uploaded_time')
    list_filter = ('doc_type',)
    ordering = ('-uploaded_time',)