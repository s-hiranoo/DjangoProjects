from django.contrib import admin

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'created_at',)
    list_display_links = ('id', 'question_text',)


admin.site.register(Question, QuestionAdmin)



class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'choice_text', 'vote',)
    list_display_links = ('id', 'choice_text',)


admin.site.register(Choice, ChoiceAdmin)
