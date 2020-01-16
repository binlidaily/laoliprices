from __future__ import unicode_literals
from django.db import models


class product_price(models.Model):
    product_id = models.AutoField(null=False, blank=False, primary_key=True)
    product_title = models.CharField(max_length=200, null=False, blank=False)
    product_spec = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True, default=1)
    unit = models.CharField(max_length=20, null=True, blank=True)
    unit_price = models.IntegerField(null=False, blank=False, default=0)
    total_price = models.IntegerField(null=True, blank=True, default=0)
    remarks = models.CharField(max_length=200, null=True, blank=True)
    