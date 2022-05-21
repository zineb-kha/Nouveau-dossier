# Generated by Django 4.0.3 on 2022-04-18 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_alter_boitiers_fournisseur'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boitiers',
            old_name='version',
            new_name='Version',
        ),
        migrations.AddField(
            model_name='carte_sim',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
