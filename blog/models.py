import datetime

from django.db import models
from django.utils import timezone

# Each model is represented by a class that subclasses django.db.models.Model.
# Each model has a number of class variables, each of which represents a database field in the model.

class Post(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    bodytext = models.TextField()
    timestamp = models.DateTimeField('date published') # Designate an optional human-readable name.
    
    def __unicode__(self):
        """ For displaying objects. """
        return self.title
    
    def was_published_recently(self):
        return self.timestamp >= timezone.now() - datetime.timedelta(weeks=4)
    was_published_recently.admin_order_field = 'timestamp'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
