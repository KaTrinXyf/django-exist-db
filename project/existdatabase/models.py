# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TbOrg(models.Model):
    id = models.IntegerField(primary_key=True)
    org_name = models.CharField(max_length=48, blank=True, null=True)
    boss_name = models.CharField(max_length=20, blank=True, null=True)
    boss_tel = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_org'


class TbUser(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(blank=True, null=True)
    org = models.ForeignKey(TbOrg, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_user'
