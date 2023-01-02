from django.db import models
from django.urls import reverse_lazy


class Menu(models.Model):
    title = models.CharField(max_length=60, verbose_name="Название")

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=60, verbose_name="Название")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='categories', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('page_with_menu', kwargs={'pk': self.title})
