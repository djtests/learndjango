from django.contrib import admin
from .models import Blog, Author
# Register your models here.



class PostAdmin(admin.ModelAdmin):
       list_display = ('id','title', 'slug', 'publish',
'status','created')
       list_filter = ('status', 'created', 'publish')
       search_fields = ('title', 'body')
       prepopulated_fields = {'slug': ('title',)}
       date_hierarchy = 'publish'
       ordering = ['status', 'publish']

admin.site.register(Blog,PostAdmin)
admin.site.register(Author)