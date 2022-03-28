# Generated by Django 3.0 on 2022-03-27 21:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_auto_20220327_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultanswers',
            name='answers',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Ответы пользователя'),
        ),
        migrations.AlterField(
            model_name='resultanswers',
            name='email',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Email пользователя'),
        ),
        migrations.AlterField(
            model_name='resultanswers',
            name='name',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='resultanswers',
            name='questuins',
            field=models.CharField(blank=True, default='0', max_length=10, null=True, verbose_name='Пройденые ответы'),
        ),
        migrations.AlterField(
            model_name='resultanswers',
            name='result_bal',
            field=models.CharField(blank=True, default=0, max_length=10, null=True, verbose_name='Результат для подсчета'),
        ),
        migrations.AlterField(
            model_name='resultanswers',
            name='userID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Идентификатор'),
        ),
    ]
