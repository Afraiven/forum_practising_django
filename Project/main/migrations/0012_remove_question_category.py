# Generated by Django 3.1.5 on 2021-01-24 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210124_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='category',
        ),
    ]