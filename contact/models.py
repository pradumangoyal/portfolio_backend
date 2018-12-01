from django.db import models

# Create your models here.
class Contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=63)
    email = models.EmailField()
    subject = models.TextField(blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    client_ip = models.CharField(max_length=63, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created',)