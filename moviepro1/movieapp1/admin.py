from django.contrib import admin

from django.contrib import admin

from.models import TeluguData,EnglishData,HindiData

class AdminTelugu(admin.ModelAdmin):
    list_display = ['movie_name','director_name','hero_name','heroine_name','producer_name','release_date']
class AdminEnglish(admin.ModelAdmin):
    list_display = ['movie_name', 'director_name', 'hero_name', 'heroine_name', 'producer_name', 'release_date']
class AdminHindi(admin.ModelAdmin):
    list_display = ['movie_name', 'director_name', 'hero_name', 'heroine_name', 'producer_name', 'release_date']
    list_display = ['movie_name', 'director_name', 'hero_name', 'heroine_name', 'producer_name', 'release_date']
admin.site.register(TeluguData,AdminTelugu)
admin.site.register(EnglishData,AdminEnglish)
admin.site.register(HindiData,AdminHindi)

