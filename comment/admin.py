from django.contrib import admin

# Register your models here.
from comment.models import Comment
from typeidea.base_admin import BaseOwnerAdmin
from typeidea.custom_site import custom_site


@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
