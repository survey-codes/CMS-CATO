from django.contrib import admin

from infrastucture.dataaccess.main.admin.base_admin import Base


class BaseInline(admin.StackedInline, Base):
    extra = 0
