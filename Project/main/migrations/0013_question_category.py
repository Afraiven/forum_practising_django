# Generated by Django 3.1.5 on 2021-01-24 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_question_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ManyToManyField(to='main.Category'),
        ),
    ]
