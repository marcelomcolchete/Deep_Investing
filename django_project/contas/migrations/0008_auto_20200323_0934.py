# Generated by Django 3.0.3 on 2020-03-23 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0007_auto_20200323_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bova11',
            name='nome',
            field=models.CharField(max_length=10, verbose_name='BOVA11.SA'),
        ),
    ]