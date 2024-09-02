# Generated by Django 5.1 on 2024-08-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_todo_category_task_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='deadline',
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
