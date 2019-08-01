from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Employees(MPTTModel):
    name = models.CharField('Name', max_length=50)
    salary = models.DecimalField('Salary', max_digits=10, decimal_places=2)
    parent = TreeForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
        db_index=True
    )
    
    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Empregado'
        verbose_name_plural = 'Empregados'
        ordering = ['name']