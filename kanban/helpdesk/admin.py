from django.contrib import admin
from helpdesk import models


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Engineer)
class EngineerAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_filename')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Priority)
class PriorityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'category', 'priority')
    search_fields = ('title',)
    list_filter = ('status', 'category', 'priority')
