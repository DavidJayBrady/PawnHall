# Generated by Django 3.0.5 on 2020-07-11 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawnlisting', '0010_auto_20200710_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='pawn',
            name='notes',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='pawn',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pawn_pictures/'),
        ),
    ]