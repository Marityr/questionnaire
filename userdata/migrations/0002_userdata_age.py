# Generated by Django 3.0 on 2022-04-17 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='age',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Возраст'),
        ),
    ]
