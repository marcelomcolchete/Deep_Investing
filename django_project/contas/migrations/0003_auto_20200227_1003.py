# Generated by Django 3.0.3 on 2020-02-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_transacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transacao',
            options={'verbose_name_plural': 'Transacoes'},
        ),
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
