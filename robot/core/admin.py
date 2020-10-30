from django.contrib import admin

from core.models import Robot


@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'creator', 'is_activated')
    fields = (
        'name',
        'description',
        'creator',
        'is_activated'
    )