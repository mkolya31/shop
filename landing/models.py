from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return "Пользователь %s" % (self.email)

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'MySubscribers'

# Create your models here.
