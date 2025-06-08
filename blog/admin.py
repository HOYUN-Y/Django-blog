from django.contrib import admin
from .models import Posts, Statements, Document, GuestbookEntry
# Register your models here.


admin.site.register(Posts)
admin.site.register(Statements)
admin.site.register(GuestbookEntry)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title','doc_type', 'uploaded_time')
    list_filter = ('doc_type',)
    ordering = ('-uploaded_time',)