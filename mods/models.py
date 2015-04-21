from django.db import models

class Mod(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    mod = models.FileField()
    owner = models.ForeignKey('auth.User', related_name='mods')
    
    class Meta:
        ordering = ('created',)
