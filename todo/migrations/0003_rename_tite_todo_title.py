# Generated by Django 3.2.2 on 2021-06-02 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_datecompleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='tite',
            new_name='title',
        ),
    ]
