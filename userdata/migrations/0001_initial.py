# Generated by Django 3.0 on 2022-04-28 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=255, null=True, verbose_name='Никнейм')),
                ('age', models.CharField(blank=True, max_length=255, null=True, verbose_name='Возраст')),
                ('gender', models.CharField(blank=True, max_length=255, null=True, verbose_name='Пол')),
                ('massa', models.CharField(blank=True, max_length=255, null=True, verbose_name='Вес')),
                ('purpose', models.CharField(blank=True, max_length=255, null=True, verbose_name='Цели')),
                ('decision', models.CharField(blank=True, max_length=255, null=True, verbose_name='Решение')),
                ('problem', models.BooleanField()),
                ('problem_two', models.BooleanField()),
                ('problem_fre', models.BooleanField()),
                ('problem_4', models.BooleanField()),
                ('problem_5', models.BooleanField()),
                ('problem_6', models.BooleanField()),
                ('problem_7', models.BooleanField()),
                ('problem_8', models.BooleanField()),
                ('problem_9', models.BooleanField()),
                ('problem_10', models.BooleanField()),
                ('problem_11', models.BooleanField()),
                ('problem_12', models.BooleanField()),
                ('problem_13', models.BooleanField()),
                ('problem_14', models.BooleanField()),
                ('problem_15', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Данные пользователя',
                'verbose_name_plural': 'Данные пользователей',
            },
        ),
    ]
