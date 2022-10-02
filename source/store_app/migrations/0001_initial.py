# Generated by Django 4.1 on 2022-10-02 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('pic', models.URLField(blank=True, default='product_pic', null=True, verbose_name='Фото')),
                ('category', models.TextField(choices=[('ELEC', 'Электроника'), ('GROS', 'Бакалея'), ('PETS', 'Зоотовары'), ('ALC', 'Алкоголь'), ('OTHER', 'Разное')], default='OTHER', max_length=20, verbose_name='Категория')),
                ('qty', models.SmallIntegerField(verbose_name='Остаток')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('changed_at', models.DateTimeField(verbose_name='Дата изменения')),
            ],
        ),
    ]
