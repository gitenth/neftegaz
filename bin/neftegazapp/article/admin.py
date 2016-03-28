from django.contrib import admin
from article.models import SkvConst, SkvHistory, Dobicha

class DobichaTabular(admin.TabularInline):
    model = Dobicha
    extra = 1

class HistoryInLine(admin.ModelAdmin):
    pass

class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        DobichaTabular,
    ]

# Register your models here.
admin.site.register(SkvConst, AuthorAdmin)
admin.site.register(SkvHistory, HistoryInLine)