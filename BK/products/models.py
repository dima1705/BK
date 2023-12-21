from django.db import models
from django.urls import reverse


class Burger(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    weight = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='burgers')

    class Meta:
        verbose_name = 'Бургер'
        verbose_name_plural = 'Бургеры'

    def __str__(self):
        return f'{self.name} | {self.price}'

    def get_absolute_url(self):
        return reverse('burger', kwargs={'burger_id': self.pk})

