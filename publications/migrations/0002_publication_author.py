# Generated by Django 3.2.9 on 2021-11-11 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='author',
            field=models.CharField(default='Anonimus', max_length=35),
        ),
    ]
