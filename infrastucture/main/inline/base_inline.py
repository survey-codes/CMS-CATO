from django.contrib import admin

from infrastucture.main.admin.base import Base


class BaseInline(admin.StackedInline, Base):
    extra = 0
