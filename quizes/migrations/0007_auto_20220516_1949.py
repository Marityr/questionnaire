# Generated by Django 3.0 on 2022-05-16 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0006_auto_20220516_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='count',
            field=models.CharField(default=1, max_length=255, verbose_name='Попытка'),
        ),
        migrations.AlterField(
            model_name='result_answers',
            name='count',
            field=models.CharField(default=1, max_length=20, verbose_name='Количество попыток'),
        ),
    ]
