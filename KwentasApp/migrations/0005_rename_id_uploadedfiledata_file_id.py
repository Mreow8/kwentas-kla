# Generated by Django 5.0.2 on 2025-04-20 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KwentasApp', '0004_alter_uploadedfiledata_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadedfiledata',
            old_name='id',
            new_name='file_id',
        ),
    ]
