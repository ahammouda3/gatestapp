from django.db import models

from datetime import datetime

class User(models.Model):
    '''
    This table is meant soley to create reliable and fast unique id's for each user
    to be used in sessions
    
    The other fields besides analytics_id may choose to be useful for speed as well.
    '''
    analytics_id = models.AutoField(primary_key=True)
    creation_time = models.DateTimeField(null=False, default=datetime.now())
    "make it a time delta to prevent end of month failure"
    expiration_time = models.DateTimeField(null=False, 
                                           default=(
            datetime(datetime.now().year, datetime.now().month, datetime.now().day +1, 0)-datetime.now() )
                                           )
