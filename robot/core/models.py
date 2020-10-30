from django.db import models

from auth_.models import MainUser


class Robot(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='projects')
    is_activated = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Robot'
        verbose_name_plural = 'Robots'

    def __str__(self):
        return f'{self.name}: {self.creator}'
