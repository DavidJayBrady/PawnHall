# Generated by Django 3.0.8 on 2020-07-22 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawnlisting', '0004_ps3pawn_ps4pawn'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ps3pawn',
            options={'verbose_name': 'PS3Pawn', 'verbose_name_plural': 'PS3 Pawns'},
        ),
        migrations.AlterModelOptions(
            name='ps4pawn',
            options={'verbose_name': 'PS4Pawn', 'verbose_name_plural': 'PS4 Pawns'},
        ),
        migrations.AddField(
            model_name='ps3pawn',
            name='psn',
            field=models.TextField(default='ps3PSN', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ps4pawn',
            name='psn',
            field=models.TextField(default='ps4PSN', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='xboxonepawn',
            name='gamertag',
            field=models.TextField(default='xb1 Gamertag', max_length=15),
            preserve_default=False,
        ),
    ]
