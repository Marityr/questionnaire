# Generated by Django 3.0 on 2022-03-31 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20220329_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='result_answers',
            name='color',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
    ]