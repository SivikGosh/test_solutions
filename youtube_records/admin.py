from django.contrib import admin

from youtube_records.models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
