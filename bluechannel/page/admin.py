from django.contrib import admin
from page.models import Highlight, Type, Event, Template, Page

class HighlightAdmin(admin.ModelAdmin):
    save_on_top = True
    pass

admin.site.register(Highlight, HighlightAdmin)

class TypeAdmin(admin.ModelAdmin):
    save_on_top = True
    pass
    
admin.site.register(Type, TypeAdmin)

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    list_display = ('name','event_start_date')
    search_fields = ('name','description')
    pass

admin.site.register(Event, EventAdmin)

class TemplateAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('name', 'description')

admin.site.register(Template, TemplateAdmin)

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    list_display = ('title', 'page_title', 'page_type', 'status', 'summary', 'author', 'updated_at', 'in_nav', 'parent')
    list_filter = ('status', 'in_nav', 'page_type')
    search_fields = ('title', 'page_title', 'summary', 'main_content')

admin.site.register(Page, PageAdmin)
