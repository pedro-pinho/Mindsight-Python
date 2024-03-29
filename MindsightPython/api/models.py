from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Employees(MPTTModel):
    name = models.CharField('Name', max_length=50, default='')
    salary = models.DecimalField('Salary', max_digits=10, decimal_places=2, default=0)
    parent = TreeForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
        db_index=True
    )

    def manager(self):
        name = self.get_ancestors(ascending=True, include_self=False).values('name')
        if name and name[0] and name[0]['name']:
            return name[0]['name']
        return None
    
    def descendants(self):
        descendants = self.get_descendants(include_self=False)
        return descendants

    def descendants_salary(self):
        descendants = self.get_descendants(include_self=False)
        salary = 0
        for descendant in descendants:
            salary += descendant.salary
        return salary

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Empregado'
        verbose_name_plural = 'Empregados'
        ordering = ['name']