# Generated by Django 2.0.5 on 2018-05-16 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treasure',
            old_name='materials',
            new_name='material',
        ),
    ]
