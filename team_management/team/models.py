from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
    
class Member(models.Model):
    
    TYPE = (
        ('ADMIN', 'Admin'),
        ('REGULAR', 'Regular'),
    )
    
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=20, choices=TYPE, null=True) 
     
    created = models.DateTimeField(null=True, blank=True, editable=False)
    modified = models.DateTimeField(null=True, blank=True) 
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.created:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Member, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.id)  