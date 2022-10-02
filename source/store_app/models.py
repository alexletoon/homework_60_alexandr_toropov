from email.policy import default
from tabnanny import verbose
from django.db import models
from django.db.models import TextChoices


class Choice(TextChoices):
    ELECTRONICS = 'ELEC', 'Электроника'
    GROCERIES = 'GROS', 'Бакалея'
    PETS = 'PETS', 'Зоотовары'
    ALCOHOL = 'ALC', 'Алкоголь'
    OTHER = 'OTHER', 'Разное'


class Product(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name="Описание", max_length=2000, null=True, blank=True)
    pic = models.URLField(verbose_name='Фото', blank=True, null=True, default='product_pic')
    category = models.TextField(verbose_name='Категория', max_length=20, null=False, blank=False, choices=Choice.choices, default=Choice.OTHER)
    qty = models.SmallIntegerField(verbose_name='Остаток', blank=False, null=False)
    price = models.DecimalField(verbose_name='Стоимость', null=False, blank=False, max_digits=7, decimal_places=2)

    
    def __str__(self) -> str:
        return f'Product - {self.name}, category - {self.category}, quantity - {self.qty}, price - {self.price}'


