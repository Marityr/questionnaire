# Generated by Django 3.0 on 2022-03-22 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='correct',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
