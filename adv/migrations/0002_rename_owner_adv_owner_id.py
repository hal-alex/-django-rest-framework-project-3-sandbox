# Generated by Django 4.1.5 on 2023-01-09 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adv', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adv',
            old_name='owner',
            new_name='owner_id',
        ),
    ]
