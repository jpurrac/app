# Generated by Django 2.2.9 on 2020-01-04 20:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inv', '0005_productos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Productos',
            new_name='Producto',
        ),
    ]
