# Generated by Django 5.1.3 on 2024-12-11 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_alter_djangomodelclass_file_path_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='djangomodelclass',
            name='file_path_field',
        ),
    ]
