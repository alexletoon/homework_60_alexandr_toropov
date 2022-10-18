from ast import Delete
from email.policy import default
from enum import auto
from tabnanny import verbose
from datetime import datetime
from django.db import models
from django.db.models import TextChoices
from django.core.validators import MinValueValidator



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
    is_deleted = models.BooleanField(verbose_name="Удалено", default=False, null=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)

    class Meta:
        ordering = ['category']
    
    def __str__(self) -> str:
        return f'Product - {self.name}, category - {self.category}, quantity - {self.qty}, price - {self.price}'


    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()


class ShoppingCart(models.Model):
    product = models.ForeignKey('store_app.Product', related_name='shopping_carts',on_delete=models.CASCADE)
    qty = models.IntegerField(verbose_name='Количество', validators=(MinValueValidator(0),), null=True, blank=True)

    def __str__(self) -> str:
        return f'Product - {self.product}, quantity - {self.qty}'


    # def delete(self,using=None, keep_parents=False):


class Order(models.Model):
    product = models.ManyToManyField('store_app.Product', related_name='order', verbose_name='Продукт в заказе')
    user_name = models.CharField(verbose_name='Имя пользователя', null=False, blank=False, max_length=200)
    telephone = models.CharField(verbose_name='Телефон', max_length=30, null=False, blank=False)
    address = models.CharField(verbose_name='Адрес', max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)


    def __str__(self) -> str:
        return f'Name - {self.user_name}, product - {self.product} '
