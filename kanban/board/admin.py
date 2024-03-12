from board import models
from django.contrib import admin


class ColumnInline(admin.TabularInline):
    model = models.Column


@admin.register(models.KanbanBoard)
class KanbanBoardAdmin(admin.ModelAdmin):
    inlines = [ColumnInline]
