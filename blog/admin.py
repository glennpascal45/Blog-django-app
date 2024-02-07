from django.contrib import admin
from django.contrib.auth.models import User, Group
from blog.models import Post


# customize the admin site
class AdminSite(admin.AdminSite):
    site_header = 'Blog Administration'
    site_title = 'Blog Administration'
    index_title = 'Blog Administration'


my_blog = AdminSite(name='my_blog')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', )
    search_fields = ('title',)
    list_filter = ('publish', 'status')
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
my_blog.register(Post, PostAdmin)
my_blog.register(User)
my_blog.register(Group)
