from django.contrib import admin
from .models import Post

# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3


class PostAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

# Register your models here.
admin.site.register(Post)
#admin.site.register(Question, QuestionAdmin)

