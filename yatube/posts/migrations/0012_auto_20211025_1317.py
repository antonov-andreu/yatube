# Generated by Django 2.2.6 on 2021-10-25 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20210807_2035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Сообщество', 'verbose_name_plural': 'Сообщества'},
        ),
    ]
