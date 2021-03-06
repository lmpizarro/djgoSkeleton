from django.contrib import admin
from skeleton.apps.polls.models import Choice, Poll

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
    readonly_fields = ("pub_date",) # http://stackoverflow.com/questions/3516799/django-modeladmin-fieldsets-field-date-missing-from-the-form

admin.site.register(Poll, PollAdmin)
