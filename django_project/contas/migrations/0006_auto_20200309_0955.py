# Generated by Django 3.0.3 on 2020-03-09 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0005_auto_20200309_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='createData',
        ),
        migrations.RemoveField(
            model_name='user',
            name='descricao',
        ),
    ]
