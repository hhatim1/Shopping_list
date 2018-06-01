# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models

# Create your models here.
class Item_Manager(models.Manager):
    def item_validation(self, postData):
        errors = {}
        if len(postData['item']) < 2:
            errors["item"] = "Item name must be more than one character."
        return errors


class Add_item(models.Model):
    item = models.CharField(max_length=255)
    added_by = models.ForeignKey(User, related_name='created_items')
    date_added = models.DateTimeField(auto_now_add=True)
    joined_by = models.ManyToManyField(User, related_name='items_joined')
    objects = Item_Manager()

    def others(self):
        return self.joined_by.exclude(id=self.created_by.id)

    def __repr__(self):
        return "{}".format(self.item)
