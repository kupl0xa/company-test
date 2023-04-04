from django.core.validators import MinValueValidator
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=150, blank=False)
    director = models.OneToOneField(
        'Employee',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='dep_director'
    )

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'
        ordering = ['id']

    def __str__(self):
        return self.name


class Employee(models.Model):
    last_name = models.CharField(max_length=150, blank=False)
    first_name = models.CharField(max_length=150, blank=False)
    surname = models.CharField(max_length=150, blank=False)
    photo = models.ImageField(
        upload_to='photos',
        blank=True
    )
    job_title = models.CharField(max_length=150, blank=False)
    age = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(
                limit_value=18,
                message='Возраст должен быть 18+ лет'
            )]
    )
    salary = models.PositiveSmallIntegerField()
    department = models.ForeignKey(
        Department,
        blank=False,
        on_delete=models.PROTECT,
        related_name='employee'
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['id']
        constraints = [
            models.UniqueConstraint(
                fields=['last_name', 'first_name', 'surname', 'department'],
                name='unique_employee-department'
            )
        ]

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    @classmethod
    def search_lastname(cls, last_name):
        return cls.objects.filter(last_name=last_name)
