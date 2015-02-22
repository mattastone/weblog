from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

