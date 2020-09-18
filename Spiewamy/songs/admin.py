from django.contrib import admin
from .models import Song

#The eaisies way to add model is
# admin.site.register(Song)  without addotional inheritance

# @admin.register(Song) # You can also add properties to class for register it imiidietly
# In this way you can register many models in the same time with the same logic
class SongAdmin(admin.ModelAdmin):
    pass
    '''
    date_hierarchy = 'created'
    list_display = ('title', 'play_on', 'text_view')
    list_display_links = ('title', 'text_view') # create link to edit this
    list_editable = ('play_on',)
    ordering = ('-created',) # dodawanie kolejności po kolumnie (- oznacza odwrotne)
    def text_view(self, obj):
        return obj.text
    '''

# Register your models here.
admin.site.register(Song, SongAdmin)