from django.contrib import admin

# Register your models here.
from .models import TbOrg, TbUser


class Org(admin.ModelAdmin):
    list_display = ['id', 'org_name', 'boss_name', 'boss_tel', 'city']


@admin.register(TbUser)
class User(admin.ModelAdmin):
    def orginfo(self):
        return self.org.org_name
    list_display = ['name', 'age', orginfo]


# 注册
admin.site.register(TbOrg, Org)
