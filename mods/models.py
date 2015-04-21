from django.db import models

class Mod(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    version = models.CharField(max_length=10)
    mod = models.FileField()
    #download = models.URLField()
    owner = models.ForeignKey('auth.User', related_name='mods')
    
    class Meta:
        ordering = ('created',)
