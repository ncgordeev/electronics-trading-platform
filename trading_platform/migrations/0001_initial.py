# Generated by Django 5.1.2 on 2024-10-29 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=10, verbose_name='Номер дома')),
                ('level', models.CharField(choices=[('0', 'Завод'), ('1', 'Розничная сеть'), ('2', 'Индивидуальный предприниматель')], verbose_name='Уровень сети')),
                ('debt', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Задолженность, руб')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients', to='trading_platform.networknode', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Узел сети',
                'verbose_name_plural': 'Узлы сети',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('model', models.CharField(max_length=200, verbose_name='Модель')),
                ('release_date', models.DateField(verbose_name='Дата выхода продукта')),
                ('network_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='trading_platform.networknode', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
