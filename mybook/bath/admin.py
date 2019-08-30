from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'done', 'reserve_time',)
    list_display_links = ('done', 'reserve_time')


admin.site.register(Member, MemberAdmin)
