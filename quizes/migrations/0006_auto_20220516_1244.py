# Generated by Django 3.0 on 2022-05-16 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0005_auto_20220516_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newansvers',
            name='quiz',
            field=models.CharField(max_length=255, verbose_name='Опросник'),
        ),
    ]
