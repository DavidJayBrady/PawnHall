# Generated by Django 3.0.8 on 2020-07-17 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pawnlisting', '0004_auto_20200717_0151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pawn',
            old_name='teriary_inclination',
            new_name='tertiary_inclination',
        ),
    ]