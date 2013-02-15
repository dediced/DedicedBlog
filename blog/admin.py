from django.contrib import admin
from blog.models import Post

# Create a model of the admin object and pass it as an argument to register().

class PostAdmin(admin.ModelAdmin):
    # The first element of each tuple in fieldsets is the title of the fieldset.
    fieldsets = [
        ('Post Content', {
            'fields': ('title', 'author', 'timestamp', 'bodytext')
        }),
    ]
    
    # Displays individual fields.
    list_display = ('title', 'author', 'timestamp', 'was_published_recently')
    
    # Adds a filter sidebar that allows the change list to be filtered by the pub_date field.
    # The type of filter displayed depends on the type of field you're filtering on.
    list_filter = ['timestamp']
    
    # Adds a search box at the top of the change list.
    search_fields = ['title']
    
    # Adds hierarchical navigation, by date, to the top of the change list page.
    date_hierarchy = 'timestamp'

admin.site.register(Post, PostAdmin)
