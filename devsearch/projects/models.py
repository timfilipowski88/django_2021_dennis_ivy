from django.db import models
import uuid
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    # null=True means we can create a Project Model instace without a description, blank=True means that our forms will know that we can submit a Project without the description.
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) # automatically creates timestamp on creation
    # Here we override the generic id with a uuid, set as unique, set as primary key, and uneditable
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # This makes it so that if we access a model without specifying an attribute, we will recieve the models title as a name for it
    def __str__(self):
        return self.title


class Review(models.Model):
    #creating a tuple
    VOTE_TYPE = {
        # value is 'up' , string version of it is 'Up Vote' 
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    }
    #owner =
    #project = models.ForeignKey()
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
