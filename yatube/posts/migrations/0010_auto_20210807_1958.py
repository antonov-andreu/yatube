# Generated by Django 2.2.6 on 2021-08-07 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_follow'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set(),
        ),
    ]
