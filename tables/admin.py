from django.contrib import admin

from task_runner.models import UserAgent
from .models import Table, TableBrand

admin.site.register(Table)
admin.site.register(TableBrand)
admin.site.register(UserAgent)
