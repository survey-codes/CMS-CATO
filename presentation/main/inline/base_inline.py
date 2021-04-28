from django.contrib import admin

from presentation.main.admin.base import Base


class BaseInline(admin.StackedInline, Base):
    extra = 0
