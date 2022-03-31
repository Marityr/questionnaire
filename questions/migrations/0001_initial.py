# Generated by Django 3.0 on 2022-03-29 00:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quizes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result_answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=200)),
                ('questions', models.CharField(max_length=500)),
                ('result', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Результат ответов',
                'verbose_name_plural': 'Результаты ответов',
            },
        ),
        migrations.CreateModel(
            name='ResultAnswers',
            fields=[
                ('userID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('name', models.CharField(max_length=10, verbose_name='Имя пользователя')),
                ('gender', models.CharField(max_length=10, verbose_name='Пол пользователя')),
                ('email', models.CharField(max_length=10, null=True, verbose_name='Email пользователя')),
            ],
            options={
                'verbose_name': 'Учасник',
                'verbose_name_plural': 'Участники',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('legend', models.TextField(blank=True, null=True, verbose_name='Легенда вопроса')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizes.Quiz')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
            ],
            options={
                'verbose_name': 'Ответы',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]