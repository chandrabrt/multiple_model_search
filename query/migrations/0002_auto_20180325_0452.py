# Generated by Django 2.0.3 on 2018-03-25 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lesson',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
