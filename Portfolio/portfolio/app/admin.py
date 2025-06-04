from django.contrib import admin
from .models import Video,Article

class VideoAdmin(admin.ModelAdmin):
    list_display = ('description', 'embed_url', 'link')
    search_fields = ('description',)

admin.site.register(Video, VideoAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'Heading','newspaper_name','newspaper_email','first_para','second_para','third_para','fourth_para','created_at')
    search_fields = ('title','newspaper_name','newspaper_email','first_para','second_para','third_para','fourth_para')

admin.site.register(Article, ArticleAdmin)
