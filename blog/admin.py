from django.contrib import admin
from .models import Post

# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pubdate','category')
    list_filter = ('pubdate',)
    # fields = ('question_text', 'pub_date')
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]

# Register your models here.
admin.site.register(Post, PostAdmin)
#admin.site.register(Question, QuestionAdmin)

