# Generated by Django 4.2 on 2023-04-04 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_department_director_alter_employee_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Департамент', 'verbose_name_plural': 'Департаменты'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
    ]