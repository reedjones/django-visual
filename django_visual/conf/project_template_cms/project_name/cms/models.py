# -*- coding: utf-8 -*-


from django.db import models


class Item(models.Model):
    """
    Content item
    """
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.title
