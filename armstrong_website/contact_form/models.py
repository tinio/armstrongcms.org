from datetime import datetime

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    
    created_at = models.DateTimeField()
   
    class Meta:
        ordering    = ['-created_at']

    def __unicode__(self): 
       return ' - '.join((self.name, self.email,)) 
   
        
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.now()
        return super(Contact, self).save(*args, **kwargs)