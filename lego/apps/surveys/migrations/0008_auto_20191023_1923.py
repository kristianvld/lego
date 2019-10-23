# Generated by Django 2.1.11 on 2019-10-23 19:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('surveys', '0007_auto_20190714_1906'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submission',
            options={'default_manager_name': 'objects'},
        ),
        migrations.AddField(
            model_name='survey',
            name='answered_by',
            field=models.ManyToManyField(blank=True, related_name='answered_surveys', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='submission',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='submission',
            name='user',
        ),
    ]
