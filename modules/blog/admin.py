from blog.models import *
from django.db.models import Count
from django.contrib import admin

class BlogPostCategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'articles',)
	
	def articles(self, obj):
		return obj.posts.count()
	
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'statut', 'category', 'author', 'pub_date',)
	date_hierarchy = 'pub_date'
	
admin.site.register(BlogPostCategory, BlogPostCategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)