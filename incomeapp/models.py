# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User



class TblIncome(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    total_income = models.IntegerField(blank=True, null=True)
    income_category = models.CharField(max_length=20, blank=True, null=True)
    income_name = models.CharField(max_length=50, null=True)
    income_value = models.IntegerField(blank=True, null=True)
    income_dt = models.DateField(blank=True, null=True)
    updated_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_income'
