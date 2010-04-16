import models
from django.contrib import admin


class NotesAdmin(admin.ModelAdmin):
    list_display = ('slug','title' , 'text')
admin.site.register(models.Note, NotesAdmin)