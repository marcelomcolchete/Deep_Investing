# Generated by Django 3.0.3 on 2020-03-24 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0009_auto_20200324_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='nome',
            field=models.CharField(max_length=10),
        ),
    ]
