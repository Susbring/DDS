from django.db import models


class FinancialMove(models.Model):
    date = models.DateField(
        verbose_name='Дата',
        auto_now_add=False,
        auto_now=False,
        help_text='Дата создания записи. Можно изменить вручную.'
    )
    status = models.ForeignKey(
        'DDSStatus',
        on_delete=models.PROTECT,
        verbose_name='Статус',
        help_text='Статус траты. Бизнес, Личное, Налог и т.д.'
    )
    type = models.ForeignKey(
        'DDSType',
        on_delete=models.PROTECT,
        verbose_name='Тип',
        help_text='Тип затраты. Списание или Пополнение'
    )
    category = models.ForeignKey(
        'DDSCategory',
        on_delete=models.PROTECT,
        verbose_name='Категория'
    )
    subcategory = models.ForeignKey(
        'DDSSubcategory',
        on_delete=models.PROTECT,
        verbose_name='Подкатегория'
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Сумма',
        help_text='Количество средств в рублях'
    )
    comment = models.CharField(
        verbose_name='Комментарий',
        max_length=100,
        blank=True,
        null=True,
        help_text='Комментарий к записи'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True
    )

    def __str__(self):
        return f'{self.date} - {self.type} - {self.category} - {self.amount}'

    class Meta:
        verbose_name = 'Записть ДДС'
        verbose_name_plural = 'Записи ДДС'
        ordering = ['-date']


class DDSStatus(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Название статуса'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус ДДС'
        verbose_name_plural = 'Статусы ДДС'


class DDSType(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Название типа'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип ДДС'
        verbose_name_plural = 'Типы ДДС'


class DDSCategory(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Название категории'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория ДДС'
        verbose_name_plural = 'Категории ДДС'


class DDSSubcategory(models.Model):
    category = models.ForeignKey(
        DDSCategory,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название подкатегории'
    )

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'Подкатегория ДДС'
        verbose_name_plural = 'Подкатегории ДДС'
        unique_together = ('category', 'name')
