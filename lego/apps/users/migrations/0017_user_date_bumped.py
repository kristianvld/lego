# Generated by Django 2.0.3 on 2018-07-29 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_abakusgroup_contact_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_bumped',
            field=models.DateTimeField(default=None, null=True, verbose_name='date bumped'),
        ),
    ]
