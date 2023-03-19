from django.contrib import admin

from infrastucture.dataaccess.main.admin.base import Base


class BaseInline(admin.StackedInline, Base):
    extra = 0
