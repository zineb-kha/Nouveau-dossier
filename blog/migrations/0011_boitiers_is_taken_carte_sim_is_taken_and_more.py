# Generated by Django 4.0.3 on 2022-05-06 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_affectation_nom_boitier_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='boitiers',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='carte_sim',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='véhicule',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
    ]
