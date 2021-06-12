# Generated by Django 2.2.10 on 2021-06-09 23:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossier',
            name='attached_files',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='dossier',
            name='decision',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='dossier',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dossier',
            name='remarks',
            field=models.CharField(max_length=250, null=True),
        ),
    ]