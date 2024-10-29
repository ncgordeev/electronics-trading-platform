from django.db import models
from django.utils.translation import gettext as _

NULLABLE = {'null': True, 'blank': True}


class NetworkNode(models.Model):
    class LevelChoices(models.TextChoices):
        """Выбор сети"""
        ZERO = '0', _('Завод')
        ONE = '1', _('Розничная сеть')
        TWO = '2', _('Индивидуальный предприниматель')

    name = models.CharField(max_length=200, verbose_name='Название')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    level = models.CharField(choices=LevelChoices, verbose_name='Уровень сети')
    supplier = models.ForeignKey('self', **NULLABLE, on_delete=models.SET_NULL, related_name='clients',
                                 verbose_name='Поставщик')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Задолженность, руб')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        verbose_name = "Узел сети"
        verbose_name_plural = "Узлы сети"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название")
    model = models.CharField(
        max_length=200,
        verbose_name="Модель")
    release_date = models.DateField(
        verbose_name="Дата выхода продукта")
    network_node = models.ForeignKey(
        NetworkNode,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Поставщик")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name} ({self.model})"
