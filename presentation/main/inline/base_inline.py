from django.contrib import admin


class BaseInline(admin.StackedInline):
    extra = 0
